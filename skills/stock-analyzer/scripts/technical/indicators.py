"""
Technical indicators module.
Computes SMA, EMA, RSI, MACD, and Bollinger Bands from scratch using pandas.
"""

import pandas as pd
import numpy as np


class TechnicalIndicators:
    """Calculate technical analysis indicators on OHLCV data."""

    def __init__(self, df):
        """
        Args:
            df: pandas DataFrame with at least 'Close', 'High', 'Low', 'Volume' columns
        """
        self.df = df
        self.close = df["Close"]

    def sma(self, period):
        """Simple Moving Average."""
        return self.close.rolling(window=period, min_periods=period).mean()

    def ema(self, period):
        """Exponential Moving Average."""
        return self.close.ewm(span=period, adjust=False).mean()

    def rsi(self, period=14):
        """
        Relative Strength Index.
        Uses smoothed moving average method (Wilder's RSI).
        """
        delta = self.close.diff()
        gain = delta.where(delta > 0, 0.0)
        loss = (-delta).where(delta < 0, 0.0)

        avg_gain = gain.rolling(window=period, min_periods=period).mean()
        avg_loss = loss.rolling(window=period, min_periods=period).mean()

        # Smoothed averages for subsequent values
        for i in range(period, len(avg_gain)):
            avg_gain.iloc[i] = (avg_gain.iloc[i - 1] * (period - 1) + gain.iloc[i]) / period
            avg_loss.iloc[i] = (avg_loss.iloc[i - 1] * (period - 1) + loss.iloc[i]) / period

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def macd(self, fast=12, slow=26, signal=9):
        """
        MACD (Moving Average Convergence Divergence).

        Returns:
            tuple of (macd_line, signal_line, histogram) as pandas Series
        """
        fast_ema = self.close.ewm(span=fast, adjust=False).mean()
        slow_ema = self.close.ewm(span=slow, adjust=False).mean()
        macd_line = fast_ema - slow_ema
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        histogram = macd_line - signal_line
        return macd_line, signal_line, histogram

    def bollinger_bands(self, period=20, std_dev=2):
        """
        Bollinger Bands.

        Returns:
            tuple of (upper, middle, lower) as pandas Series
        """
        middle = self.sma(period)
        rolling_std = self.close.rolling(window=period, min_periods=period).std()
        upper = middle + (rolling_std * std_dev)
        lower = middle - (rolling_std * std_dev)
        return upper, middle, lower

    def compute_all(self):
        """
        Compute all standard indicators.

        Returns:
            dict of indicator name -> pandas Series
        """
        indicators = {}

        # Moving averages
        indicators["sma_20"] = self.sma(20)
        indicators["sma_50"] = self.sma(50)
        indicators["sma_200"] = self.sma(200)

        # RSI
        indicators["rsi"] = self.rsi(14)

        # MACD
        macd_line, signal_line, histogram = self.macd()
        indicators["macd"] = macd_line
        indicators["macd_signal"] = signal_line
        indicators["macd_hist"] = histogram

        # Bollinger Bands
        upper, middle, lower = self.bollinger_bands()
        indicators["bb_upper"] = upper
        indicators["bb_middle"] = middle
        indicators["bb_lower"] = lower

        return indicators
