# Stock Analyzer

A comprehensive stock analysis skill that provides technical indicators, trading signals, chart generation, and news sentiment analysis.

## Usage

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/stock-analyzer/scripts/main.py --ticker SYMBOL [options]
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--ticker` | Stock ticker symbol (required) | - |
| `--period` | Data period: 1mo, 3mo, 6mo, 1y, 2y, 5y, max | 6mo |
| `--interval` | Data interval: 1d, 1wk, 1mo | 1d |
| `--technical` | Include technical indicator columns in history output | false |
| `--no-cache` | Bypass cache and fetch fresh data | false |

### Multi-Market Support

| Suffix | Market | Currency |
|--------|--------|----------|
| (none) | United States | USD |
| .HK | Hong Kong | HKD |
| .SS | China (Shanghai) | CNY |
| .SZ | China (Shenzhen) | CNY |
| .L | United Kingdom | GBP |
| .T | Japan | JPY |

## Technical Indicators

- **SMA** (20, 50, 200 periods) - Simple Moving Averages
- **RSI** (14 periods) - Relative Strength Index
- **MACD** (12/26/9) - Moving Average Convergence Divergence with signal line and histogram
- **Bollinger Bands** (20 periods, 2 standard deviations)

## Trading Signals

Signals are generated using a scoring system (-5 to +5):

- **RSI**: Overbought (>70) / Oversold (<30)
- **MACD**: Bullish / Bearish crossover
- **Bollinger Bands**: Price position relative to bands
- **Trend**: Price vs SMA 50 (+/- 2% threshold)
- **SMA Crossover**: Golden cross / Death cross (SMA 20 vs SMA 50)

Recommendations: Strong Buy, Buy, Hold, Sell, Strong Sell

## Output

JSON object containing:
- `metadata` - Ticker, market, currency, timestamp
- `price` - Current price, OHLCV, change, change %
- `technical_indicators` - Latest values for all indicators
- `signals` - Trading signals with overall recommendation
- `chart` - Path to generated candlestick chart PNG
- `sentiment` - News headline sentiment analysis
- `history` - Historical OHLCV data

## Example Queries

- "Analyze the recent performance of AAPL"
- "Is TSLA a good buy right now based on technicals?"
- "Show me the 1-year chart for MSFT with indicators"
- "What's the sentiment around NVDA?"

## Dependencies

```
pip install -r requirements.txt
```

Requires: yfinance, pandas, mplfinance, textblob
