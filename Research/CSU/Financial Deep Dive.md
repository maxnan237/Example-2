# Constellation Software Inc. (CSU) — Financial Deep Dive

*Analysis date: 2026-07-02 | Primary sources: Q4/FY2025 audited financial statements (dated March 9, 2026) and Q4/FY2025 MD&A, cross-checked against Q4/FY2024 financial statements*

---

## Accounting Basis

[CSU_Q4FY2025_FinancialStatements.pdf, page 4/8]: "These consolidated financial statements have been prepared in accordance with IFRS Accounting Standards ('IFRS') as issued by the International Accounting Standards Board." Audited by KPMG LLP (Vaughan, Canada). **Reporting/functional currency is U.S. dollars** [page 15, Note 2(c)] — despite Canadian incorporation and TSX listing. All figures below are US$ millions unless noted.

**Important structural note:** CSU "aggregates the six operating segments into one reportable segment" under IFRS 8 [page 56, Note 23] — no segment-level revenue or operating income is disclosed. CSU also does not present a traditional "cost of revenue / gross profit / SG&A" income statement — it uses IFRS nature-of-expense presentation (staff costs, hardware, third-party license/maintenance, occupancy, travel, professional fees, depreciation, amortization).

---

## 1. Income Statement (US$ million)

[CSU_Q4FY2025_FinancialStatements.pdf, page 9] and [CSU_Q4FY2024_FinancialStatements.pdf, page 9]:

| $M | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| License revenue | 386 | 393 | 415 |
| Professional services revenue | 1,766 | 1,975 | 2,126 |
| Hardware and other revenue | 268 | 302 | 382 |
| Maintenance and other recurring revenue | 5,985 | 7,396 | 8,700 |
| **Total revenue** | **8,407** | **10,066** | **11,623** |
| Staff costs | 4,493 | 5,322 | 5,924 |
| Amortization of intangible assets | 859 | 1,044 | 1,182 |
| Depreciation | 162 | 182 | 201 |
| Other operating costs (hardware, 3rd-party license/maint., occupancy, travel, professional fees, other) | 1,705 | 2,054 | 2,421 |
| **Total expenses** | **7,219** | **8,602** | **9,728** |
| Foreign exchange loss (gain) | 43 | (26) | 154 |
| IRGA/TSS membership liability revaluation charge | 152 | 183 | 440 |
| Finance and other expense (income) | (34) | (60) | (228) |
| Bargain purchase gain | (54) | (10) | (10) |
| Impairment of intangible/other non-financial assets | 26 | 28 | 43 |
| Redeemable preferred securities expense (income) | 597 | 58 | 0 |
| Revaluation of equity-method investment to cost | — | — | 260 |
| Finance costs | 192 | 280 | 297 |
| **Income before income taxes** | **265** | **1,011** | **939** |
| Income tax expense | 204 | 244 | 353 |
| **Net income** | **62** | **767** | **586** |
| — attributable to common shareholders | 565 | 731 | 512 |
| — attributable to non-controlling interests | (503) | 37 | 74 |
| Diluted EPS | $26.67 | $34.48 | $24.15 |

**A note on volatility in this income statement:** CSU's reported net income and EPS are meaningfully affected each year by large, non-operating fair-value/revaluation items that are NOT part of the core VMS operating business:
- FY2023: a $597M "redeemable preferred securities expense" (a fair-value charge tied to Lumine's WideOrbit-acquisition preferred shares, later converted to common in March 2024) drove consolidated net income down to just $62M and pushed net income attributable to non-controlling interests to **negative $503M** — an accounting artifact, not an operating loss.
- FY2025: a $440M "IRGA/TSS membership liability revaluation charge" (driven by rising Topicus maintenance revenue and Sygnity/Asseco equity valuations) plus a $260M "revaluation of equity-method investment to cost" charge (related to CSU's Asseco Poland S.A. stake crossing a 24.84% controlling-influence threshold, triggering a switch from FVOCI to equity-method accounting) together reduced FY2025 income before tax by $700M relative to what it otherwise would have been.

Given this volatility, **diluted EPS should not be read as a clean, comparable operating metric year-over-year** without adjusting for these large, disclosed one-time items — see [[Valuation Check]] for the practical implications on P/E interpretation.

**R&D expense:** [CSU_Q4FY2025_FinancialStatements.pdf, page 14, Note 3(iii)]: "For the year ended December 31, 2025, $1,668 (2024 – $1,489) of research and development costs have been expensed in profit or loss," net of investment tax credits of $56M (2025) / $63M (2024). FY2023 figure not found in available filings (not disclosed in the documents reviewed for this report).

---

## 2. Cash Flow Statement (US$ million)

[CSU_Q4FY2025_FinancialStatements.pdf, page 13] and [CSU_Q4FY2024_FinancialStatements.pdf, page 12]:

| $M | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Net cash flows from operating activities** | **1,779** | **2,196** | **2,732** |
| **Acquisition of businesses (cash paid)** | **(1,609)** | **(1,347)** | **(1,227)** |
| Cash obtained with acquired businesses | 152 | 164 | 173 |
| Post-acquisition settlement payments, net | (238) | (336) | (286) |
| Property and equipment purchased (capex) | (42) | (67) | (68) |
| Purchases of investments and other assets | (23) | (8) | (580) |
| **Net cash flows from investing activities** | **(1,639)** | **(1,567)** | **(1,881)** |
| Dividends paid to common shareholders | (85) | (85) | (85) |
| Proceeds from issuance of Senior Notes | — | 1,000 | — |
| Proceeds/(repayments) of debt without recourse to CSI, net | 165 | 232 | 440 |
| **Net cash flows from financing activities** | **316** | **114** | **156** |
| Cash, end of period | 1,284 | 1,980 | 3,089 |

**"Cash paid for acquisitions"** — the single most important line for a serial acquirer — was $1,609M (FY2023), $1,347M (FY2024), and $1,227M (FY2025). This has trended down over the three years reviewed even as operating cash flow has grown substantially, which is worth watching: is CSU finding fewer attractively-priced acquisition opportunities, or simply being more selective? [[Bear Case]] explores this further.

**Free Cash Flow Available to Shareholders ("FCFA2S")** — CSU's own disclosed non-IFRS metric [CSU_Q4FY2025_MDA.pdf, pages 1, 12]: defined as net cash flows from operating activities less interest paid (debt and leases), debt transaction costs, the IRGA/TSS membership liability revaluation charge, and capex, plus interest/dividends received, less the portion attributable to non-controlling interests.

| | FY2024 | FY2025 |
|---|---|---|
| **FCFA2S** | **$1,472M** | **$1,683M** |

FY2023 FCFA2S: not found in available filings (not disclosed in the documents reviewed). CSU does not repurchase shares — capital return is via a small, flat quarterly dividend only (see Section 7).

---

## 3. Balance Sheet (US$ million)

[CSU_Q4FY2025_FinancialStatements.pdf, page 8] and [CSU_Q4FY2024_FinancialStatements.pdf, page 7]:

| $M | Dec 31, 2023 | Dec 31, 2024 | Dec 31, 2025 |
|---|---|---|---|
| Cash and cash equivalents | 1,284 | 1,980 | 3,089 |
| Total assets | 10,862 | 12,848 | 16,171 |
| Intangible assets, net (incl. goodwill) | 6,675 | 7,455 | 8,388 |
| — of which Goodwill | 1,262 | 1,451 | 1,781 |
| Debt with recourse to CSI | 1,724 | 1,769 | 1,489 |
| Debt without recourse to CSI | 1,610 | 2,008 | 2,642 |
| Liability of CSI under the IRGA | n/a | 693 | 1,234 |
| Redeemable preferred securities (current) | 814 | 0 | 0 |
| **Total equity** | **1,961** | **3,288** | **4,267** |
| — Retained earnings | 1,876 | 2,919 | 3,347 |
| — Non-controlling interests | 85 | 493 | 692 |

**Total debt (as defined in MD&A, excludes the IRGA liability):** [CSU_Q4FY2025_MDA.pdf, page 17]: "Debt with recourse to Constellation Software Inc. 1,489 / 1,466... Debt without recourse to Constellation Software Inc. 2,642 / 2,008... **Debt 4,131 / 3,474**" (Dec 31, 2025 / Dec 31, 2024). **Cash less debt** (net debt): $(1,043)M (FY2025) vs. $(1,494)M (FY2024) — CSU is in a modest net-debt position by this narrower definition, though it holds $3,089M of cash against total assets of $16,171M and total debt of ~$4.1B (well covered by cash flow, [[Management Review]]).

The **IRGA liability** ($1,234M, 2025) is a Euro-denominated (€1,050M) redemption obligation to the Joday Group tied to Topicus maintenance revenue and Sygnity/Asseco equity values — a quasi-liability specific to CSU's Topicus corporate structure, not conventional bank/bond debt.

---

## 4. Segment / Entity-Level Profitability

As noted above, CSU discloses **no segment-level revenue or operating income** for its six operating groups — all aggregated into one IFRS 8 reportable segment. Voluntary supplemental disclosure exists only for Topicus, Lumine, and Altera (see [[Business Overview]], Section 2, for the full FY2025 breakdown table). Individual figures for Perseus, N. Harris, Vela, Jonas, or Volaris (ex-Lumine) are not found in available filings.

---

## 5. Debt Schedule

[CSU_Q4FY2025_FinancialStatements.pdf, Notes 11-12] and [CSU_Q4FY2025_MDA.pdf, pages 18-22]:

**Debt with recourse to CSI (Dec 31, 2025):**

| Facility | Principal | Carrying value | Terms |
|---|---|---|---|
| CSI Facility | $0 drawn | $0 | $1,085M limit (increased from $840M, Jan 2024); unsecured; variable rate |
| Senior Notes | $1,000M | $994M | $500M @ 5.158% due 2029 + $500M @ 5.461% due 2034; issued Feb 2024 |
| Debentures | $361M (C$495M) | $408M | Due March 2040; 8.9% (Mar 2025-Mar 2026) → 8.6% (Mar 2026-Mar 2027) → resets to CPI + 6.5% (floor 0%) thereafter |
| Term Loan | $87M (£65M) | $87M | Fixed rate; due 2028 |

**Debt without recourse to CSI (Dec 31, 2025):**

| Facility | Principal | Carrying value |
|---|---|---|
| Topicus Revolving Credit Facility | $393M | $391M |
| Various subsidiary debt facilities | $1,770M | $1,751M |
| Optimal Blue Promissory Note | $500M | $500M (7% p.a., matures 2063) |

Annual minimum repayment schedule for non-recourse debt facilities (excl. Topicus RCF/Promissory Note): 2026 – $199M; 2027 – $500M; 2028 – $401M; 2029 – $164M; 2030 – $372M; 2031 – $3M; 2032 – $131M.

[CSU_Q4FY2025_FinancialStatements.pdf, page 36]: A debt-covenant breach occurred in 2025 on a $51M term loan at one subsidiary, reclassified as current — described as administrative in nature, unrelated to financial performance.

---

## 6. Share Count & Capital Structure

[CSU_Q4FY2025_FinancialStatements.pdf, page 44, Note 17]: "December 31, 2025 — 21,191,530 [common shares]; December 31, 2024 — 21,191,530" — **share count unchanged year over year**, confirming CSU's famously small, static share base (unusual among the companies in this research vault, where dilution or buybacks are typically material). No preferred shares outstanding. No formal dividend reinvestment plan (DRIP) for common shares was found in the documents reviewed — not found in available filings, contrary to some external commentary.

---

## 7. Dividend History

[CSU_Q4FY2025_FinancialStatements.pdf, Note 17] and [CSU_Q4FY2025_MDA.pdf, pages 3, 30]: Quarterly dividend of **$1.00/share** in each quarter of both FY2024 and FY2025 — **$4.00/share annual dividend, unchanged year over year.** Total dividends paid to common shareholders: $85M (FY2023), $85M (FY2024), $85M (FY2025) — flat, consistent with the static share count.

[CSU_Q4FY2025_FinancialStatements.pdf, Note 29]: Subsequent event — "On March 6, 2026, the Company declared a $1.00 per share dividend payable on April 15, 2026," continuing the same rate.

[CSU_Q4FY2025_FinancialStatements.pdf, Note 20]: "The Board of Directors has adopted a policy to pay quarterly dividends, which commenced in 2012... There is no guarantee that dividends will continue to be declared and paid in the future." At current levels, the dividend is a token capital return (well under 1% yield at CSU's share price) — not a primary component of the investment thesis; nearly all excess cash flow is instead redeployed into acquisitions.

---

## 8. Impairments, One-Time Items, and Organic Growth

- **Goodwill impairment:** $11M (FY2025) vs. $7M (FY2024) — modest relative to a $1,781M goodwill balance.
- **Impairment of intangible/other non-financial assets:** $43M (FY2025), $28M (FY2024), $26M (FY2023).
- **One-time items driving income-statement volatility:** see Section 1 above — the FY2023 redeemable preferred securities expense ($597M), and the FY2025 IRGA revaluation charge ($440M) plus Asseco equity-method revaluation ($260M), are the standout items.
- **Organic growth** (CSU's key disclosed non-GAAP KPI): [CSU_Q4FY2025_MDA.pdf, page 4]: full-year FY2025 organic growth was approximately **4% (unadjusted) / 3% (FX-adjusted)**. Quarterly figures show a clear reacceleration through 2025: unadjusted organic growth was 0% (Q1 2025), 5% (Q2 2025), 5% (Q3 2025), 6% (Q4 2025) — a positive trend after bottoming in Q1 2025.
- **Backlog:** $7,700M of contracted-not-yet-recognized revenue as of Dec 31, 2025, ~61% expected within 12 months [[Business Overview]].

Not found in available filings: full-year FY2023 organic growth rate (only the Q4 2023 quarterly figure of 6% unadjusted / 4% FX-adjusted was available from the documents reviewed).
