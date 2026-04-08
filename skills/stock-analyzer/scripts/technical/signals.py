"""
Trading signal generator.
Produces buy/sell/hold signals based on technical indicators using a scoring system.
"""


class SignalGenerator:
    """Generate trading signals from technical indicators."""

    def __init__(self, df, indicators):
        """
        Args:
            df: pandas DataFrame with OHLCV data
            indicators: dict of indicator name -> pandas Series
        """
        self.df = df
        self.indicators = indicators
        self.latest_close = float(df["Close"].iloc[-1])

    def generate(self):
        """
        Generate trading signals with an overall recommendation.

        Score range: -5 (Strong Sell) to +5 (Strong Buy)

        Returns:
            dict with individual signals and overall recommendation
        """
        signals = []
        score = 0

        # RSI signal
        if "rsi" in self.indicators:
            rsi_val = float(self.indicators["rsi"].dropna().iloc[-1])
            if rsi_val > 70:
                signals.append({"indicator": "RSI", "value": round(rsi_val, 2), "signal": "Overbought", "action": "sell"})
                score -= 1
            elif rsi_val < 30:
                signals.append({"indicator": "RSI", "value": round(rsi_val, 2), "signal": "Oversold", "action": "buy"})
                score += 1
            else:
                signals.append({"indicator": "RSI", "value": round(rsi_val, 2), "signal": "Neutral", "action": "hold"})

        # MACD signal
        if "macd" in self.indicators and "macd_signal" in self.indicators:
            macd_val = float(self.indicators["macd"].dropna().iloc[-1])
            signal_val = float(self.indicators["macd_signal"].dropna().iloc[-1])
            if macd_val > signal_val:
                signals.append({"indicator": "MACD", "value": round(macd_val, 4), "signal": "Bullish crossover", "action": "buy"})
                score += 1
            else:
                signals.append({"indicator": "MACD", "value": round(macd_val, 4), "signal": "Bearish crossover", "action": "sell"})
                score -= 1

        # Bollinger Bands signal
        if "bb_upper" in self.indicators and "bb_lower" in self.indicators:
            bb_upper = float(self.indicators["bb_upper"].dropna().iloc[-1])
            bb_lower = float(self.indicators["bb_lower"].dropna().iloc[-1])
            if self.latest_close > bb_upper:
                signals.append({"indicator": "Bollinger Bands", "signal": "Above upper band", "action": "sell"})
                score -= 1
            elif self.latest_close < bb_lower:
                signals.append({"indicator": "Bollinger Bands", "signal": "Below lower band", "action": "buy"})
                score += 1
            else:
                signals.append({"indicator": "Bollinger Bands", "signal": "Within bands", "action": "hold"})

        # Trend signal (price vs SMA 50)
        if "sma_50" in self.indicators:
            sma_50 = self.indicators["sma_50"].dropna()
            if not sma_50.empty:
                sma_50_val = float(sma_50.iloc[-1])
                pct_diff = ((self.latest_close - sma_50_val) / sma_50_val) * 100
                if pct_diff > 2:
                    signals.append({"indicator": "Trend (SMA 50)", "value": round(sma_50_val, 2), "signal": "Above SMA 50", "action": "buy"})
                    score += 1
                elif pct_diff < -2:
                    signals.append({"indicator": "Trend (SMA 50)", "value": round(sma_50_val, 2), "signal": "Below SMA 50", "action": "sell"})
                    score -= 1
                else:
                    signals.append({"indicator": "Trend (SMA 50)", "value": round(sma_50_val, 2), "signal": "Near SMA 50", "action": "hold"})

        # SMA crossover (SMA 20 vs SMA 50)
        if "sma_20" in self.indicators and "sma_50" in self.indicators:
            sma_20 = self.indicators["sma_20"].dropna()
            sma_50 = self.indicators["sma_50"].dropna()
            if not sma_20.empty and not sma_50.empty:
                sma_20_val = float(sma_20.iloc[-1])
                sma_50_val = float(sma_50.iloc[-1])
                if sma_20_val > sma_50_val:
                    signals.append({"indicator": "SMA Crossover", "signal": "Golden cross (SMA 20 > SMA 50)", "action": "buy"})
                    score += 1
                else:
                    signals.append({"indicator": "SMA Crossover", "signal": "Death cross (SMA 20 < SMA 50)", "action": "sell"})
                    score -= 1

        # Overall recommendation
        if score >= 3:
            recommendation = "Strong Buy"
        elif score >= 1:
            recommendation = "Buy"
        elif score <= -3:
            recommendation = "Strong Sell"
        elif score <= -1:
            recommendation = "Sell"
        else:
            recommendation = "Hold"

        return {
            "score": score,
            "recommendation": recommendation,
            "details": signals,
        }
