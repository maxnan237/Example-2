"""
Data fetcher module - retrieves stock data via yfinance.
"""

import yfinance as yf
import pandas as pd


class DataFetcher:
    """Fetches stock price data and metadata from Yahoo Finance."""

    def fetch(self, ticker, period="6mo", interval="1d"):
        """
        Fetch historical OHLCV data.

        Args:
            ticker: Stock ticker symbol
            period: Data period (1mo, 3mo, 6mo, 1y, 2y, 5y, max)
            interval: Data interval (1d, 1wk, 1mo)

        Returns:
            pandas DataFrame with OHLCV data, or None on failure
        """
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(period=period, interval=interval)
            if df.empty:
                return None
            # Ensure standard column names
            df.columns = [c.title() if c.islower() else c for c in df.columns]
            return df
        except Exception:
            return None

    def get_info(self, ticker):
        """
        Get stock metadata (name, sector, market cap, etc.).

        Args:
            ticker: Stock ticker symbol

        Returns:
            dict with stock info
        """
        try:
            stock = yf.Ticker(ticker)
            return stock.info or {}
        except Exception:
            return {}

    def get_news(self, ticker, limit=5):
        """
        Get recent news headlines for the ticker.

        Args:
            ticker: Stock ticker symbol
            limit: Maximum number of headlines

        Returns:
            list of dicts with 'title' and 'publisher' keys
        """
        try:
            stock = yf.Ticker(ticker)
            news = stock.news or []
            results = []
            for item in news[:limit]:
                results.append({
                    "title": item.get("title", ""),
                    "publisher": item.get("publisher", ""),
                    "link": item.get("link", ""),
                })
            return results
        except Exception:
            return []
