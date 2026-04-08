#!/usr/bin/env python3
"""
Stock Analyzer - ai-align/finance-plugin
A comprehensive stock analysis tool with technical indicators, sentiment analysis,
and chart generation.

Usage:
    python3 main.py --ticker AAPL [--period 6mo] [--interval 1d] [--technical] [--no-cache]
"""

import argparse
import json
import sys
import os
from datetime import datetime

from core.data_fetcher import DataFetcher
from technical.indicators import TechnicalIndicators
from technical.signals import SignalGenerator
from sentiment.news_sentiment import NewsSentimentAnalyzer
from utils.cache import CacheManager
from utils.chart import ChartGenerator


def parse_args():
    parser = argparse.ArgumentParser(description="Stock Analyzer - Technical & Fundamental Analysis")
    parser.add_argument("--ticker", required=True, help="Stock ticker symbol (e.g., AAPL, 0700.HK, 600519.SS)")
    parser.add_argument("--period", default="6mo", choices=["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"],
                        help="Data period (default: 6mo)")
    parser.add_argument("--interval", default="1d", choices=["1d", "1wk", "1mo"],
                        help="Data interval (default: 1d)")
    parser.add_argument("--technical", action="store_true",
                        help="Include technical indicator columns in history output")
    parser.add_argument("--no-cache", action="store_true",
                        help="Bypass cache and fetch fresh data")
    return parser.parse_args()


def detect_market(ticker):
    """Detect market based on ticker suffix."""
    ticker_upper = ticker.upper()
    if ticker_upper.endswith(".HK"):
        return {"market": "Hong Kong", "currency": "HKD"}
    elif ticker_upper.endswith(".SS"):
        return {"market": "China (Shanghai)", "currency": "CNY"}
    elif ticker_upper.endswith(".SZ"):
        return {"market": "China (Shenzhen)", "currency": "CNY"}
    elif ticker_upper.endswith(".L"):
        return {"market": "United Kingdom", "currency": "GBP"}
    elif ticker_upper.endswith(".T"):
        return {"market": "Japan", "currency": "JPY"}
    else:
        return {"market": "United States", "currency": "USD"}


def main():
    args = parse_args()
    ticker = args.ticker.upper()
    market_info = detect_market(ticker)

    # Determine cache directory relative to plugin root
    plugin_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    cache_dir = os.path.join(plugin_root, "data", "cache")

    cache = CacheManager(cache_dir)

    # Fetch data
    fetcher = DataFetcher()
    cache_key = f"{ticker}_{args.period}_{args.interval}"

    if not args.no_cache:
        cached = cache.get(cache_key)
        if cached is not None:
            df = cached
        else:
            df = fetcher.fetch(ticker, period=args.period, interval=args.interval)
            if df is not None and not df.empty:
                cache.set(cache_key, df)
    else:
        df = fetcher.fetch(ticker, period=args.period, interval=args.interval)

    if df is None or df.empty:
        print(json.dumps({"error": f"No data found for ticker: {ticker}"}))
        sys.exit(1)

    # Get stock info
    info = fetcher.get_info(ticker)

    # Calculate technical indicators
    ti = TechnicalIndicators(df)
    indicators = ti.compute_all()

    # Generate trading signals
    sg = SignalGenerator(df, indicators)
    signals = sg.generate()

    # Generate chart
    chart_gen = ChartGenerator(cache_dir)
    chart_path = chart_gen.generate(ticker, df, indicators, args.period)

    # Sentiment analysis
    sentiment_analyzer = NewsSentimentAnalyzer()
    news = fetcher.get_news(ticker)
    sentiment = sentiment_analyzer.analyze(news)

    # Build price summary
    latest = df.iloc[-1]
    prev_close = df.iloc[-2]["Close"] if len(df) > 1 else latest["Close"]
    change = latest["Close"] - prev_close
    change_pct = (change / prev_close) * 100 if prev_close != 0 else 0

    price_summary = {
        "current": round(float(latest["Close"]), 2),
        "open": round(float(latest["Open"]), 2),
        "high": round(float(latest["High"]), 2),
        "low": round(float(latest["Low"]), 2),
        "volume": int(latest["Volume"]),
        "change": round(change, 2),
        "change_pct": round(change_pct, 2),
    }

    # Build history output
    history = []
    for idx, row in df.iterrows():
        entry = {
            "date": idx.strftime("%Y-%m-%d") if hasattr(idx, "strftime") else str(idx),
            "open": round(float(row["Open"]), 2),
            "high": round(float(row["High"]), 2),
            "low": round(float(row["Low"]), 2),
            "close": round(float(row["Close"]), 2),
            "volume": int(row["Volume"]),
        }
        if args.technical:
            for key, series in indicators.items():
                if hasattr(series, "iloc"):
                    val = series.get(idx)
                    entry[key] = round(float(val), 4) if val is not None and not (isinstance(val, float) and val != val) else None
        history.append(entry)

    # Build final result
    result = {
        "metadata": {
            "ticker": ticker,
            "name": info.get("shortName", ticker),
            "market": market_info["market"],
            "currency": market_info["currency"],
            "period": args.period,
            "interval": args.interval,
            "timestamp": datetime.now().isoformat(),
        },
        "price": price_summary,
        "technical_indicators": {
            "sma_20": round(float(indicators["sma_20"].iloc[-1]), 4) if "sma_20" in indicators and not indicators["sma_20"].empty else None,
            "sma_50": round(float(indicators["sma_50"].iloc[-1]), 4) if "sma_50" in indicators and not indicators["sma_50"].empty else None,
            "sma_200": round(float(indicators["sma_200"].iloc[-1]), 4) if "sma_200" in indicators and not indicators["sma_200"].empty else None,
            "rsi_14": round(float(indicators["rsi"].iloc[-1]), 2) if "rsi" in indicators and not indicators["rsi"].empty else None,
            "macd": {
                "macd": round(float(indicators["macd"].iloc[-1]), 4) if "macd" in indicators else None,
                "signal": round(float(indicators["macd_signal"].iloc[-1]), 4) if "macd_signal" in indicators else None,
                "histogram": round(float(indicators["macd_hist"].iloc[-1]), 4) if "macd_hist" in indicators else None,
            },
            "bollinger_bands": {
                "upper": round(float(indicators["bb_upper"].iloc[-1]), 4) if "bb_upper" in indicators else None,
                "middle": round(float(indicators["bb_middle"].iloc[-1]), 4) if "bb_middle" in indicators else None,
                "lower": round(float(indicators["bb_lower"].iloc[-1]), 4) if "bb_lower" in indicators else None,
            },
        },
        "signals": signals,
        "chart": chart_path,
        "sentiment": sentiment,
        "history": history,
    }

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
