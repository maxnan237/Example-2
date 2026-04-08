"""
Chart generator module.
Creates multi-panel candlestick charts with technical indicator overlays.
"""

import os


class ChartGenerator:
    """Generate stock analysis charts using mplfinance."""

    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate(self, ticker, df, indicators, period):
        """
        Generate a multi-panel chart with price, volume, RSI, and MACD.

        Args:
            ticker: Stock ticker symbol
            df: pandas DataFrame with OHLCV data
            indicators: dict of indicator name -> pandas Series
            period: Data period string

        Returns:
            str: Path to the generated chart PNG, or None on failure
        """
        try:
            import mplfinance as mpf
            import matplotlib
            matplotlib.use("Agg")
        except ImportError:
            return None

        chart_path = os.path.join(self.output_dir, f"{ticker}_{period}_chart.png")

        try:
            # Build additional plots
            add_plots = []

            # SMA overlays
            if "sma_20" in indicators:
                sma_20 = indicators["sma_20"].reindex(df.index)
                add_plots.append(mpf.make_addplot(sma_20, color="blue", width=0.8, label="SMA 20"))
            if "sma_50" in indicators:
                sma_50 = indicators["sma_50"].reindex(df.index)
                add_plots.append(mpf.make_addplot(sma_50, color="orange", width=0.8, label="SMA 50"))

            # Bollinger Bands
            if "bb_upper" in indicators and "bb_lower" in indicators:
                bb_upper = indicators["bb_upper"].reindex(df.index)
                bb_lower = indicators["bb_lower"].reindex(df.index)
                add_plots.append(mpf.make_addplot(bb_upper, color="gray", linestyle="dashed", width=0.5))
                add_plots.append(mpf.make_addplot(bb_lower, color="gray", linestyle="dashed", width=0.5))

            # RSI panel
            if "rsi" in indicators:
                rsi = indicators["rsi"].reindex(df.index)
                add_plots.append(mpf.make_addplot(rsi, panel=2, color="purple", ylabel="RSI", width=0.8))

            # MACD panel
            if "macd" in indicators and "macd_signal" in indicators:
                macd = indicators["macd"].reindex(df.index)
                macd_signal = indicators["macd_signal"].reindex(df.index)
                macd_hist = indicators["macd_hist"].reindex(df.index)
                add_plots.append(mpf.make_addplot(macd, panel=3, color="blue", ylabel="MACD", width=0.8))
                add_plots.append(mpf.make_addplot(macd_signal, panel=3, color="red", width=0.8))
                add_plots.append(mpf.make_addplot(macd_hist, panel=3, type="bar", color="dimgray", width=0.6))

            # Generate chart
            mpf.plot(
                df,
                type="candle",
                style="charles",
                title=f"\n{ticker} - {period}",
                volume=True,
                addplot=add_plots if add_plots else None,
                savefig=dict(fname=chart_path, dpi=150, bbox_inches="tight"),
                figscale=1.3,
                panel_ratios=(6, 2, 2, 2) if add_plots else (3, 1),
            )

            return chart_path
        except Exception:
            return None
