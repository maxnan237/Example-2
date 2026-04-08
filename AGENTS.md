# Finance Plugin - Agent Instructions

## Stock Analyzer

Use the stock-analyzer skill to analyze stocks. Run:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/stock-analyzer/scripts/main.py --ticker SYMBOL
```

### Setup

Install dependencies first:

```bash
pip install -r skills/stock-analyzer/requirements.txt
```

### Available Skills

- **stock-analyzer**: Technical analysis, trading signals, charts, and sentiment for any stock ticker.
