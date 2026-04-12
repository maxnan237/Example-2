# Equity Research Skill

A Claude Code skill that produces a complete long-term equity research package for any public company. Given a ticker symbol, it:

1. Looks up the company on SEC EDGAR
2. Downloads the latest 3 years of annual filings (10-K, 40-F, or 20-F)
3. Launches parallel sub-agents to extract business data, financials, and external research
4. Writes 10 standardized research documents
5. Generates a polished PDF investment memo
6. Commits everything to the `Research/{TICKER}/` folder
7. Updates the vault index at `Research/README.md`
8. Creates and merges a pull request (optional)

## Usage

```
/equity-research TICKER
/equity-research TICKER --years=5
/equity-research TICKER --skip-pdf
/equity-research TICKER --skip-commit --skip-pr
```

### Examples

```
/equity-research NVDA       # Standard run
/equity-research AAPL       # Apple
/equity-research BRK.B      # Berkshire (use dot in ticker as shown)
/equity-research SHOP       # Canadian company (will use 40-F filer framework)
```

## Output

The skill creates this structure:

```
Research/{TICKER}/
├── Business Overview.md
├── Industry Scan.md
├── Financial Deep Dive.md
├── Moat Analysis.md
├── Management Review.md
├── Valuation Check.md
├── Bear Case.md
├── Decision Log.md
├── {TICKER} Investment Memo.md
├── {TICKER} Investment Memo.pdf
├── Earnings/
│   └── {Latest Quarter}.md
└── Filings/
    ├── {TICKER}_10K_FY{YEAR}.htm
    └── ...
```

And updates `Research/README.md` to include the new company in the vault index.

## Framework

The skill follows the long-term equity analyst framework described in the project's `CLAUDE.md`:

- **Source discipline** — every factual claim cites the filing
- **Sector-adapted analysis** — REITs, miners, SaaS each get tailored treatment
- **Stance required** — Monitor / Constructive / Speculative / Income Play / Value Play / Avoid
- **Three-scenario valuation** — Bull / Base / Bear with fair values

## Runtime

A full research package takes approximately **15-20 minutes** of wall time — most of which is sub-agents processing large SEC filings. You can continue using Claude Code on other tasks while it runs.

## Cost

Each run consumes roughly the same tokens as a medium-sized Claude Code session. No additional API setup required.

## Structure

- **SKILL.md** — Main instruction file Claude reads when the skill is invoked
- **templates/** — Markdown templates guiding document structure
- **scripts/generate_pdf.py** — PDF generator using markdown + weasyprint
- **README.md** — This file

## Customization

To tailor the skill for your preferences:

- Edit templates in `templates/` to change document structure
- Edit CSS in `scripts/generate_pdf.py` to restyle the PDF
- Edit `SKILL.md` to adjust the workflow (e.g., skip certain documents, change folder names, add new sections)
