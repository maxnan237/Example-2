---
name: equity-research
description: Produce a complete long-term equity research package for a public company. Given a ticker symbol, downloads the latest SEC filings, researches the company externally, writes 10 standardized research documents, generates a PDF investment memo, and commits everything to the Research/{TICKER}/ folder.
---

# Equity Research Skill

You are a long-term equity analyst. Given a ticker symbol (e.g., `NVDA`, `AAPL`), produce a complete investment research package following the framework described below.

## Argument Parsing

Parse the user's input for:
- **TICKER** (required) — stock ticker symbol (uppercase)
- **--years=N** (optional, default 3) — how many years of filings to download
- **--skip-pdf** (optional) — skip PDF generation
- **--skip-commit** (optional) — skip git commit and push
- **--skip-pr** (optional) — skip creating/merging a pull request

If the user only provides a ticker, use defaults.

## Output Location

All outputs go in `Research/{TICKER}/` in the current repo, following this structure:

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
│   └── {latest quarter}.md
└── Filings/
    └── {TICKER}_10K_FY{YEAR}.htm (or 40-F for Canadian filers)
```

## Step-by-Step Workflow

### Step 1: Find Company on SEC EDGAR

Use `WebFetch` to search EDGAR:

```
https://efts.sec.gov/LATEST/search-index?q=%22{COMPANY_OR_TICKER}%22&forms=10-K,40-F,20-F
```

Extract:
- **CIK** (Central Index Key)
- **Company name**
- **Form type** (10-K for US, 40-F for Canadian, 20-F for other foreign)
- **Filing dates** and accession numbers for the last N years

If multiple matches, pick the one matching the ticker. If the CIK lookup is ambiguous, ask the user to confirm.

### Step 2: Download Filings

For each filing year:

1. Fetch the filing directory: `https://www.sec.gov/Archives/edgar/data/{CIK}/{ACCESSION_NO_NO_DASHES}/`
2. Identify the main document (largest `.htm` file, typically `{ticker}-{date}.htm`)
3. For 40-F filers: also download the exhibit files (ex99-1.htm, ex99-2.htm, ex99-3.htm) — these contain the AIF, MD&A, and financial statements
4. Download with User-Agent header:

```bash
curl -s -o Research/{TICKER}/Filings/{TICKER}_10K_FY{YEAR}.htm \
  -H "User-Agent: analyst@example.com" \
  "{URL}"
```

**Commit the filings immediately** after download (per the stop-hook git-check policy):
```bash
git add Research/{TICKER}/Filings/
git commit -m "Add {TICKER} filings from SEC EDGAR"
git push -u origin $(git rev-parse --abbrev-ref HEAD)
```

### Step 3: Launch Parallel Research Agents

Use three `Agent` tool calls in parallel (one message, multiple tool uses):

**Agent 1 — Business & Products Extractor**
Instructs a sonnet-model sub-agent to extract verbatim from the filings:
- Business overview (Item 1 / AIF)
- Business segments (revenue, margins)
- Revenue model and pricing
- Customer base and concentration
- Geographic breakdown
- Competitive landscape (named competitors)
- Key products or projects
- Regulatory environment
- Employees
- Key risk factors (top 10)
- Moat-relevant factors (patents, accreditation, switching costs)

**Agent 2 — Financial Statements Extractor**
Extracts 3-year data:
- Income statement (revenue by segment, costs, operating income, net income)
- Cash flow statement (OpCF, Capex, FCF, financing)
- Balance sheet (cash, debt, equity, key items)
- Segment profitability
- Debt schedule with maturities
- Share count history / dilution
- Dividend history
- Any going-concern or impairment flags

**Agent 3 — External Market Research**
Uses WebSearch and WebFetch to gather:
- Current stock price and market cap
- Valuation multiples (P/E, EV/EBITDA, P/FCF, dividend yield, P/NAV for miners)
- Peer comparison (list 3-5 relevant peers with multiples)
- Industry size and growth rate
- Most recent quarterly earnings (actual vs. consensus)
- Analyst consensus (ratings, price targets)
- Recent news (last 6 months)
- CEO background and compensation
- Insider ownership and recent transactions
- Stock performance (1-year, 3-year)

Each agent prompt should include:
- File paths to read
- The Python HTML stripping pattern: `re.sub(r'<[^>]+>', ' ', content)`
- Instructions to return verbatim quotes with source attribution
- Request for exact dollar amounts, not rounded

### Step 4: Write Research Documents

Use the templates in `.claude/skills/equity-research/templates/` as structural guides. For each company, produce these 8 core documents:

1. **Business Overview.md** — what the company does, segments, customers, dependencies
2. **Industry Scan.md** — market size, growth, competitors, regulatory environment
3. **Financial Deep Dive.md** — multi-year P&L, cash flow, balance sheet, accounting flags
4. **Moat Analysis.md** — switching costs, network effects, cost advantages, intangibles, efficient scale; trajectory (Widening/Stable/Narrowing); summary paragraph
5. **Management Review.md** — leadership, capital allocation, insider activity, guidance credibility, overall assessment
6. **Valuation Check.md** — current multiples, peer comps, scenario framework (Bull/Base/Bear with fair values)
7. **Bear Case.md** — thesis killer, structural weaknesses, assumptions at risk, permanent impairment scenarios, "what would prove the bear right" table
8. **Decision Log.md** — watch list with alert thresholds, decision framework, stance, key triggers

Plus:

9. **Earnings/{Quarter}.md** — most recent quarterly results analysis (Guidance vs. Reality, KPI trends, What Changed)
10. **{TICKER} Investment Memo.md** — 3-5 page synthesized summary following the memo template

### Adapt the Framework to the Company Type

Different companies need different emphasis:

| Company Type | Adjustments |
|---|---|
| **Operating company** (AVGO, UBER) | Standard framework; focus on margins, growth, competition |
| **REIT** (VICI) | Emphasize FFO/AFFO, portfolio composition, tenant concentration, lease structure, P/FFO multiple, dividend coverage |
| **Development-stage miner** (ODV) | Emphasize reserves/resources, feasibility study economics (NPV, IRR, AISC), capex funding status, dilution history, P/NAV; financial metrics less meaningful |
| **Financial institution** | Emphasize NIM, credit quality, regulatory capital ratios |
| **SaaS / Subscription** | Emphasize ARR, retention, NRR, CAC, LTV |
| **Canadian filer (40-F)** | Report in CAD under IFRS; note currency; AIF replaces Item 1 |
| **Going concern** | Flag prominently; highlight dilution risk |

### Source Discipline (CRITICAL)

Follow `CLAUDE.md` rules strictly:
- Every factual claim cites: `[filename, section]: "exact quote"`
- External data clearly flagged: `(Note: from external source X — not from uploaded filings)`
- "Not found in available filings" if data is missing
- Never fill gaps with training data
- Mark inferences explicitly: `(inferred from [source])`

### Step 5: Generate PDF Investment Memo

Use the script at `.claude/skills/equity-research/scripts/generate_pdf.py`:

```bash
python3 .claude/skills/equity-research/scripts/generate_pdf.py \
  "Research/{TICKER}/{TICKER} Investment Memo.md" \
  "Research/{TICKER}/{TICKER} Investment Memo.pdf"
```

If the script fails (e.g., weasyprint not installed), fall back to inline Python using the stock format (see script source).

Skip this step if `--skip-pdf` flag was provided.

### Step 6: Update Vault README

Open `Research/README.md` and add the new company:

1. Increment the "X companies covered" counter
2. Add a row to the **Portfolio Comparison** table
3. Add a row to the **Moat & Valuation Matrix**
4. Add a new company section with wiki-links to all documents
5. Add entries in the **Thematic Index** sections (by sector, by stance, by risk)

If `Research/README.md` doesn't exist yet, create it using the template at `.claude/skills/equity-research/templates/vault_readme.md`.

### Step 7: Commit and Push

Skip if `--skip-commit` flag was provided. Otherwise:

```bash
git add Research/{TICKER}/ Research/README.md
git commit -m "Add {TICKER} investment research package

[Summary of key findings in 2-3 lines]

https://claude.ai/code/session_{SESSION_ID}"

git push -u origin $(git rev-parse --abbrev-ref HEAD)
```

### Step 8: Create Pull Request (optional)

Skip if `--skip-pr` flag was provided OR if the current branch is `main`.

Use the GitHub MCP tools to:
1. Create a PR from the current branch to `main`
2. Merge the PR (squash merge)

Handle merge conflicts on the `Research/README.md` by keeping the feature branch version (it has the new company).

### Step 9: Summarize for User

End with a brief summary showing:
- Company name, ticker
- Market cap, current price
- Stance (Monitor / Constructive / Speculative / etc.)
- 3-5 bullet key findings
- Link to the main Investment Memo
- Any data gaps or risk flags

## Error Handling

- **Ticker not found on EDGAR** → ask user if the company is private or uses a different filer name
- **Too few years of filings available** → work with what's available, note the limitation
- **Filing too large to process** → use the exhibit approach (for 40-F) or focus on the MD&A section
- **Foreign private issuer (20-F)** → adapt to IFRS / non-USD reporting
- **PDF generation fails** → skip PDF, note in summary
- **Git push fails** → retry with exponential backoff per the branch policy; don't create PR if push fails

## Usage Examples

```
/equity-research NVDA
/equity-research AAPL --years=5
/equity-research BRK.B --skip-pdf
/equity-research SHOP --skip-commit --skip-pr
```

## Key Quality Bars

Before finishing, verify:

- [ ] All 8 core documents + earnings + memo written
- [ ] Every financial number has a filing citation
- [ ] Stance is stated with explicit reasoning
- [ ] Bear case is genuine, not softened
- [ ] Valuation includes all three scenarios with numbers
- [ ] Moat analysis rates all 5 sources explicitly
- [ ] Vault README updated to reflect new company
- [ ] PDF rendered cleanly (or reason noted if skipped)
- [ ] Committed and pushed to remote

## Notes on Sub-Agent Usage

- **Always launch the 3 research agents in parallel** (one message with multiple Agent tool calls) — this is ~3x faster than sequential
- Use `subagent_type: "general-purpose"` and `model: "sonnet"` for extraction agents
- Give each agent enough context to be self-directed — it won't have your conversation history
- Budget ~15-20 minutes of wall time for a full research package (mostly waiting for agents)
