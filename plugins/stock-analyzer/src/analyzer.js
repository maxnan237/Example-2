/**
 * Stock Analyzer - Core analysis module
 * Provides technical analysis indicators and stock data analysis.
 */

class StockAnalyzer {
  constructor(config = {}) {
    this.defaultPeriod = config.period || 14;
    this.data = [];
  }

  /**
   * Load price data for analysis.
   * @param {Array<{date: string, open: number, high: number, low: number, close: number, volume: number}>} data
   */
  loadData(data) {
    this.data = data.sort((a, b) => new Date(a.date) - new Date(b.date));
    return this;
  }

  /**
   * Calculate Simple Moving Average (SMA).
   * @param {number} period - Number of periods
   * @param {string} field - Price field to use (default: 'close')
   * @returns {Array<{date: string, value: number}>}
   */
  sma(period = this.defaultPeriod, field = 'close') {
    const results = [];
    for (let i = period - 1; i < this.data.length; i++) {
      const slice = this.data.slice(i - period + 1, i + 1);
      const avg = slice.reduce((sum, d) => sum + d[field], 0) / period;
      results.push({ date: this.data[i].date, value: parseFloat(avg.toFixed(4)) });
    }
    return results;
  }

  /**
   * Calculate Exponential Moving Average (EMA).
   * @param {number} period - Number of periods
   * @param {string} field - Price field to use (default: 'close')
   * @returns {Array<{date: string, value: number}>}
   */
  ema(period = this.defaultPeriod, field = 'close') {
    const k = 2 / (period + 1);
    const results = [];

    // Start with SMA for the first value
    const firstSlice = this.data.slice(0, period);
    let prevEma = firstSlice.reduce((sum, d) => sum + d[field], 0) / period;
    results.push({ date: this.data[period - 1].date, value: parseFloat(prevEma.toFixed(4)) });

    for (let i = period; i < this.data.length; i++) {
      const ema = this.data[i][field] * k + prevEma * (1 - k);
      prevEma = ema;
      results.push({ date: this.data[i].date, value: parseFloat(ema.toFixed(4)) });
    }
    return results;
  }

  /**
   * Calculate Relative Strength Index (RSI).
   * @param {number} period - Number of periods (default: 14)
   * @returns {Array<{date: string, value: number}>}
   */
  rsi(period = this.defaultPeriod) {
    const results = [];
    const changes = [];

    for (let i = 1; i < this.data.length; i++) {
      changes.push(this.data[i].close - this.data[i - 1].close);
    }

    let avgGain = 0;
    let avgLoss = 0;

    // Initial average gain/loss
    for (let i = 0; i < period; i++) {
      if (changes[i] >= 0) avgGain += changes[i];
      else avgLoss += Math.abs(changes[i]);
    }
    avgGain /= period;
    avgLoss /= period;

    let rs = avgLoss === 0 ? 100 : avgGain / avgLoss;
    let rsi = 100 - 100 / (1 + rs);
    results.push({ date: this.data[period].date, value: parseFloat(rsi.toFixed(2)) });

    // Subsequent values using smoothed averages
    for (let i = period; i < changes.length; i++) {
      const gain = changes[i] >= 0 ? changes[i] : 0;
      const loss = changes[i] < 0 ? Math.abs(changes[i]) : 0;

      avgGain = (avgGain * (period - 1) + gain) / period;
      avgLoss = (avgLoss * (period - 1) + loss) / period;

      rs = avgLoss === 0 ? 100 : avgGain / avgLoss;
      rsi = 100 - 100 / (1 + rs);
      results.push({ date: this.data[i + 1].date, value: parseFloat(rsi.toFixed(2)) });
    }

    return results;
  }

  /**
   * Calculate MACD (Moving Average Convergence Divergence).
   * @param {number} fastPeriod - Fast EMA period (default: 12)
   * @param {number} slowPeriod - Slow EMA period (default: 26)
   * @param {number} signalPeriod - Signal line period (default: 9)
   * @returns {Array<{date: string, macd: number, signal: number, histogram: number}>}
   */
  macd(fastPeriod = 12, slowPeriod = 26, signalPeriod = 9) {
    const fastEma = this.ema(fastPeriod);
    const slowEma = this.ema(slowPeriod);

    // Align dates and calculate MACD line
    const macdLine = [];
    const slowDates = new Set(slowEma.map((d) => d.date));

    for (const fast of fastEma) {
      if (slowDates.has(fast.date)) {
        const slow = slowEma.find((d) => d.date === fast.date);
        macdLine.push({
          date: fast.date,
          value: parseFloat((fast.value - slow.value).toFixed(4)),
        });
      }
    }

    // Calculate signal line (EMA of MACD)
    const k = 2 / (signalPeriod + 1);
    const results = [];

    if (macdLine.length < signalPeriod) return results;

    let signalEma =
      macdLine.slice(0, signalPeriod).reduce((sum, d) => sum + d.value, 0) / signalPeriod;

    results.push({
      date: macdLine[signalPeriod - 1].date,
      macd: macdLine[signalPeriod - 1].value,
      signal: parseFloat(signalEma.toFixed(4)),
      histogram: parseFloat((macdLine[signalPeriod - 1].value - signalEma).toFixed(4)),
    });

    for (let i = signalPeriod; i < macdLine.length; i++) {
      signalEma = macdLine[i].value * k + signalEma * (1 - k);
      results.push({
        date: macdLine[i].date,
        macd: macdLine[i].value,
        signal: parseFloat(signalEma.toFixed(4)),
        histogram: parseFloat((macdLine[i].value - signalEma).toFixed(4)),
      });
    }

    return results;
  }

  /**
   * Calculate Bollinger Bands.
   * @param {number} period - Number of periods (default: 20)
   * @param {number} stdDevMultiplier - Standard deviation multiplier (default: 2)
   * @returns {Array<{date: string, upper: number, middle: number, lower: number}>}
   */
  bollingerBands(period = 20, stdDevMultiplier = 2) {
    const smaValues = this.sma(period);
    const results = [];

    for (let i = period - 1; i < this.data.length; i++) {
      const slice = this.data.slice(i - period + 1, i + 1);
      const mean = slice.reduce((sum, d) => sum + d.close, 0) / period;
      const variance = slice.reduce((sum, d) => sum + Math.pow(d.close - mean, 2), 0) / period;
      const stdDev = Math.sqrt(variance);

      results.push({
        date: this.data[i].date,
        upper: parseFloat((mean + stdDevMultiplier * stdDev).toFixed(4)),
        middle: parseFloat(mean.toFixed(4)),
        lower: parseFloat((mean - stdDevMultiplier * stdDev).toFixed(4)),
      });
    }

    return results;
  }

  /**
   * Calculate Average True Range (ATR).
   * @param {number} period - Number of periods (default: 14)
   * @returns {Array<{date: string, value: number}>}
   */
  atr(period = this.defaultPeriod) {
    const trueRanges = [];

    for (let i = 1; i < this.data.length; i++) {
      const high = this.data[i].high;
      const low = this.data[i].low;
      const prevClose = this.data[i - 1].close;
      const tr = Math.max(high - low, Math.abs(high - prevClose), Math.abs(low - prevClose));
      trueRanges.push({ date: this.data[i].date, value: tr });
    }

    const results = [];
    if (trueRanges.length < period) return results;

    let atr = trueRanges.slice(0, period).reduce((sum, d) => sum + d.value, 0) / period;
    results.push({ date: trueRanges[period - 1].date, value: parseFloat(atr.toFixed(4)) });

    for (let i = period; i < trueRanges.length; i++) {
      atr = (atr * (period - 1) + trueRanges[i].value) / period;
      results.push({ date: trueRanges[i].date, value: parseFloat(atr.toFixed(4)) });
    }

    return results;
  }

  /**
   * Calculate On-Balance Volume (OBV).
   * @returns {Array<{date: string, value: number}>}
   */
  obv() {
    const results = [];
    if (this.data.length === 0) return results;

    let obv = 0;
    results.push({ date: this.data[0].date, value: obv });

    for (let i = 1; i < this.data.length; i++) {
      if (this.data[i].close > this.data[i - 1].close) {
        obv += this.data[i].volume;
      } else if (this.data[i].close < this.data[i - 1].close) {
        obv -= this.data[i].volume;
      }
      results.push({ date: this.data[i].date, value: obv });
    }

    return results;
  }

  /**
   * Generate a summary analysis report.
   * @returns {{trend: string, indicators: object, signals: Array<string>}}
   */
  analyze() {
    if (this.data.length < 26) {
      throw new Error('Insufficient data: at least 26 data points required for full analysis');
    }

    const latestPrice = this.data[this.data.length - 1].close;
    const sma20 = this.sma(20);
    const sma50 = this.sma(50);
    const rsiValues = this.rsi(14);
    const macdValues = this.macd();
    const bbands = this.bollingerBands(20);

    const latestSma20 = sma20.length > 0 ? sma20[sma20.length - 1].value : null;
    const latestSma50 = sma50.length > 0 ? sma50[sma50.length - 1].value : null;
    const latestRsi = rsiValues.length > 0 ? rsiValues[rsiValues.length - 1].value : null;
    const latestMacd = macdValues.length > 0 ? macdValues[macdValues.length - 1] : null;
    const latestBB = bbands.length > 0 ? bbands[bbands.length - 1] : null;

    const signals = [];

    // Trend determination
    let trend = 'neutral';
    if (latestSma20 && latestSma50) {
      if (latestPrice > latestSma20 && latestSma20 > latestSma50) trend = 'bullish';
      else if (latestPrice < latestSma20 && latestSma20 < latestSma50) trend = 'bearish';
    }

    // RSI signals
    if (latestRsi !== null) {
      if (latestRsi > 70) signals.push('RSI indicates overbought conditions');
      else if (latestRsi < 30) signals.push('RSI indicates oversold conditions');
    }

    // MACD signals
    if (latestMacd) {
      if (latestMacd.histogram > 0) signals.push('MACD histogram is positive (bullish momentum)');
      else signals.push('MACD histogram is negative (bearish momentum)');
    }

    // Bollinger Band signals
    if (latestBB) {
      if (latestPrice > latestBB.upper)
        signals.push('Price is above upper Bollinger Band (potentially overbought)');
      else if (latestPrice < latestBB.lower)
        signals.push('Price is below lower Bollinger Band (potentially oversold)');
    }

    return {
      price: latestPrice,
      trend,
      indicators: {
        sma20: latestSma20,
        sma50: latestSma50,
        rsi: latestRsi,
        macd: latestMacd,
        bollingerBands: latestBB,
      },
      signals,
    };
  }
}

module.exports = { StockAnalyzer };
