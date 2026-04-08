/**
 * ai-align/finance-plugin: stock-analyzer
 *
 * A stock analysis plugin providing technical indicators and analysis tools.
 * Includes SMA, EMA, RSI, MACD, Bollinger Bands, ATR, and OBV calculations.
 */

const { StockAnalyzer } = require('./src/analyzer');
const { Formatter } = require('./src/formatter');

const PLUGIN_NAME = 'stock-analyzer';
const PLUGIN_VERSION = '1.0.0';

/**
 * Plugin registration entry point.
 * @param {object} context - Plugin context provided by the host application
 * @returns {object} Plugin interface
 */
function register(context = {}) {
  const config = {
    period: 14,
    ...context.config,
  };

  const analyzer = new StockAnalyzer(config);

  return {
    name: PLUGIN_NAME,
    version: PLUGIN_VERSION,

    /**
     * Run a full analysis on the provided stock data.
     * @param {string} symbol - Ticker symbol
     * @param {Array} priceData - OHLCV price data
     * @param {object} options - Analysis options
     * @returns {object} Analysis results
     */
    analyze(symbol, priceData, options = {}) {
      analyzer.loadData(priceData);
      const analysis = analyzer.analyze();
      const format = options.format || 'json';

      if (format === 'text') {
        return Formatter.textReport(symbol, analysis);
      }
      return { symbol: symbol.toUpperCase(), ...analysis };
    },

    /**
     * Calculate a specific technical indicator.
     * @param {string} indicator - Indicator name (sma, ema, rsi, macd, bollingerBands, atr, obv)
     * @param {Array} priceData - OHLCV price data
     * @param {object} params - Indicator parameters
     * @returns {Array} Indicator values
     */
    indicator(indicator, priceData, params = {}) {
      analyzer.loadData(priceData);
      const method = analyzer[indicator];
      if (typeof method !== 'function') {
        throw new Error(`Unknown indicator: ${indicator}. Available: sma, ema, rsi, macd, bollingerBands, atr, obv`);
      }
      return method.call(analyzer, ...Object.values(params));
    },

    /**
     * Export indicator data as CSV.
     * @param {Array} data - Indicator data points
     * @returns {string} CSV string
     */
    toCsv(data) {
      return Formatter.toCsv(data);
    },
  };
}

module.exports = { register, StockAnalyzer, Formatter };
