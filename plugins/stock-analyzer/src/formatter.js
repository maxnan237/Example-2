/**
 * Output formatter for stock analysis results.
 */

class Formatter {
  /**
   * Format analysis results as a plain-text report.
   * @param {string} symbol - Stock ticker symbol
   * @param {object} analysis - Analysis result from StockAnalyzer.analyze()
   * @returns {string}
   */
  static textReport(symbol, analysis) {
    const lines = [
      `=== Stock Analysis: ${symbol.toUpperCase()} ===`,
      `Price: $${analysis.price.toFixed(2)}`,
      `Trend: ${analysis.trend.toUpperCase()}`,
      '',
      '--- Indicators ---',
    ];

    const { indicators } = analysis;

    if (indicators.sma20 !== null) lines.push(`SMA(20): $${indicators.sma20.toFixed(2)}`);
    if (indicators.sma50 !== null) lines.push(`SMA(50): $${indicators.sma50.toFixed(2)}`);
    if (indicators.rsi !== null) lines.push(`RSI(14): ${indicators.rsi}`);
    if (indicators.macd) {
      lines.push(`MACD: ${indicators.macd.macd} | Signal: ${indicators.macd.signal} | Histogram: ${indicators.macd.histogram}`);
    }
    if (indicators.bollingerBands) {
      const bb = indicators.bollingerBands;
      lines.push(`Bollinger Bands: Upper=$${bb.upper.toFixed(2)} | Mid=$${bb.middle.toFixed(2)} | Lower=$${bb.lower.toFixed(2)}`);
    }

    if (analysis.signals.length > 0) {
      lines.push('', '--- Signals ---');
      analysis.signals.forEach((s) => lines.push(`* ${s}`));
    }

    return lines.join('\n');
  }

  /**
   * Format analysis results as JSON.
   * @param {string} symbol - Stock ticker symbol
   * @param {object} analysis - Analysis result from StockAnalyzer.analyze()
   * @returns {string}
   */
  static jsonReport(symbol, analysis) {
    return JSON.stringify({ symbol: symbol.toUpperCase(), ...analysis }, null, 2);
  }

  /**
   * Format indicator data as CSV.
   * @param {Array<object>} data - Array of indicator data points
   * @returns {string}
   */
  static toCsv(data) {
    if (data.length === 0) return '';
    const headers = Object.keys(data[0]);
    const rows = data.map((row) => headers.map((h) => row[h]).join(','));
    return [headers.join(','), ...rows].join('\n');
  }
}

module.exports = { Formatter };
