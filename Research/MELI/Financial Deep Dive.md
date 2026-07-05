# MercadoLibre, Inc. (MELI) — Financial Deep Dive

*Analysis date: 2026-07-02 | Primary source: Form 10-K FY2025 (filed February 2026), cross-checked against FY2024 and FY2023 10-Ks*

---

## Accounting Basis

MELI reports under U.S. GAAP in USD millions. **Hyperinflation note (Argentina):** [MELI_10K_FY2025.htm, Note 2]: "As of July 1, 2018, the Company transitioned its Argentine operations to highly inflationary status in accordance with U.S. GAAP, and changed the functional currency for Argentine subsidiaries from Argentine Pesos to U.S. dollars." This means MELI does **not** apply IAS 29-style price-level restatement (as an IFRS filer would) — instead, Argentine-peso-denominated transactions are remeasured directly into USD, with currency effects flowing through the "Foreign currency losses, net" line rather than a discrete "monetary gain/loss" line item. Argentina's annual inflation was 31.5% (2025), 117.8% (2024), and 211.4% (2023); the official ARS/USD exchange rate moved +41.0%, +27.7%, and +356.3% over the same years, respectively.

---

## 1. Income Statement (USD million)

[MELI_10K_FY2025.htm, Consolidated Statements of Income]:

| $M | FY2023 (recast) | FY2024 | FY2025 |
|---|---|---|---|
| Net service revenues and financial income | 13,617 | 18,638 | 25,286 |
| Net product revenues | 1,490 | 2,139 | 3,607 |
| **Net revenues and financial income** | **15,107** | **20,777** | **28,893** |
| Cost of net revenues and financial expenses | (7,517) | (11,200) | (16,035) |
| **Gross profit** | **7,590** | **9,577** | **12,858** |
| Product and technology development | (1,831) | (1,934) | (2,269) |
| Sales and marketing | (1,736) | (2,191) | (3,219) |
| Provision for doubtful accounts | (1,050) | (1,858) | (3,091) |
| General and administrative | (766) | (963) | (1,078) |
| **Income from operations** | **2,207** | **2,631** | **3,201** |
| Foreign currency losses, net | (615) | (182) | (337) |
| Pretax income | 1,553 | 2,432 | 2,842 |
| Income tax expense | (569) | (521) | (845) |
| **Net income** | **987** | **1,911** | **1,997** |
| Diluted EPS | $19.46 | $37.69 | $39.40 |
| Diluted weighted-avg shares (M) | 51.0 | 50.7 | 50.7 |

Revenue grew 39.1% YoY in FY2025, but operating income grew only 21.7% (2,631→3,201) — a meaningfully slower growth rate than revenue, driven by rapidly rising provisioning costs and sales/marketing spend. **Provision for doubtful accounts grew from $1,050M (FY2023) to $3,091M (FY2025), a 194% increase over two years**, rising from 7.0% to 10.7% of total revenue — the single largest driver of the operating-margin gap between revenue growth and operating-income growth.

**Gross margin held roughly steady** (50.2% FY2023 → 46.1% FY2024 → 44.5% FY2025, calculated) — a modest decline, less dramatic than the operating-line pressure, indicating the margin compression is concentrated in credit provisioning and marketing spend below the gross-profit line, not in the core cost-of-revenue structure.

---

## 2. Cash Flow Statement (USD million)

[MELI_10K_FY2025.htm, Consolidated Statements of Cash Flows]:

| $M | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Net cash from operating activities | 5,140 | 7,918 | 12,116 |
| Capex (property/equipment/intangibles) | (509) | (860) | (1,343) |
| **Free cash flow (calculated: OpCF − capex)** | **4,631** | **7,058** | **10,773** |
| Net cash used in investing activities | (3,450) | (8,287) | (6,179) |
| Net cash from financing activities | (267) | 1,959 | 2,904 |

Both operating cash flow and free cash flow have grown strongly and consistently — FCF more than doubled from $4,631M (FY2023) to $10,773M (FY2025). Note that MELI's gross financing cash flows are unusually large relative to net financing flows — "Proceeds from loans payable and other financial liabilities" of $44,050M and "Payments on loans payable" of $41,088M in FY2025 alone — because the credit/lending business is funded through frequent short-duration debt issuance and repayment, not because MELI itself is highly leveraged in a traditional sense.

[MELI_10K_FY2025.htm]: "Cash paid for interest $611 [2025] $456 [2024] $608 [2023]"; "Cash paid for income tax $1,013 [2025] $1,052 [2024] $651 [2023]."

**No formal share-buyback program is disclosed.** The small annual "Common Stock repurchased" figures ($1M in both FY2024 and FY2025, $356M in FY2023) reflect treasury-share transactions related to RSU net-share-settlement and the 2023 convertible-note capped-call settlement, not an open-market repurchase program — not found in available filings as a board-authorized buyback authorization.

---

## 3. Balance Sheet (USD million)

[MELI_10K_FY2025.htm, Consolidated Balance Sheets], cross-checked against [MELI_10K_FY2024.htm] for the FY2023 column:

| $M | FY2023 (recast) | FY2024 | FY2025 |
|---|---|---|---|
| Cash + short-term investments | 6,036 | 7,120 | 6,299 |
| Total loans receivable, net | 2,694 | 4,895 | 9,365 |
| Total assets | 17,612 | 25,196 | 42,667 |
| Total debt | 4,495 | 5,715 | 9,193 |
| Total liabilities | 14,541 | 20,845 | 35,919 |
| **Total equity** | **3,071** | **4,351** | **6,748** |

Total assets nearly doubled from FY2024 to FY2025 ($25.2bn→$42.7bn), driven substantially by the credit portfolio more than doubling ($4.9bn→$9.4bn) and a large jump in restricted cash (used to collateralize lending-related debt facilities). Total debt grew proportionally ($5.7bn→$9.2bn) — the balance sheet is scaling primarily to fund the credit business, not general corporate purposes.

---

## 4. Segment Profitability (by Geography)

[MELI_10K_FY2025.htm, Note 8]:

| Segment | FY2023 Revenue / Direct Contribution | FY2024 Revenue / Direct Contribution | FY2025 Revenue / Direct Contribution |
|---|---|---|---|
| Brazil | $7,821M / $1,861M | $11,406M / $2,286M | $15,201M / $2,075M |
| Mexico | $3,071M / $700M | $4,664M / $854M | $6,475M / $1,171M |
| Argentina | $3,550M / $1,680M | $3,818M / $1,675M | $5,962M / $2,481M |
| Other | $665M / $50M | $889M / $117M | $1,255M / $176M |

**Brazil's direct contribution margin actually declined YoY in FY2025** ($2,286M→$2,075M) despite 33.3% revenue growth — direct segment-level evidence that the competitive intensity described in [[Industry Scan]] (Amazon, Shopee, Temu pressure in Brazil specifically) is showing up in the numbers, not just in external commentary. Argentina, by contrast, saw both revenue and direct contribution grow strongly, likely benefiting from high nominal interest rates on its credit book and currency dynamics.

---

## 5. Credit / Lending Portfolio Detail

[MELI_10K_FY2025.htm, Note 5]:

| Category (FY2025) | Gross | Allowance | Net |
|---|---|---|---|
| Merchant | $2,009M | $(747)M | $1,262M |
| Consumer | $4,559M | $(1,271)M | $3,288M |
| Credit cards | $5,656M | $(1,107)M | $4,549M |
| Asset-backed | $284M | $(18)M | $266M |
| **Total** | **$12,508M** | **$(3,143)M** | **$9,365M** |

**Allowance as % of gross portfolio (calculated):** 28.7% (FY2023) → 25.5% (FY2024) → 25.1% (FY2025) — modestly improving, but still an unusually high allowance ratio in absolute terms, reflecting the underlying credit risk profile of unsecured consumer/merchant lending in emerging markets.

[MELI_10K_FY2025.htm, Note 5]: "Renegotiations represented 1.6% (2025) and 1.4% (2024) of the loans receivable portfolio" — the closest disclosed analog to a non-performing-loan ratio; MELI does not disclose a formally labeled NPL percentage. Not found in available filings: an explicit "non-performing loan ratio."

**The declining NIMAL metric (36.2%→28.2%→22.4%, FY2023-FY2025, [[Business Overview]]) combined with rising provisioning ($1,050M→$3,091M) is the central financial risk signal in this filing** — the credit book is growing extremely fast (net loans nearly doubling annually) while its profitability-per-dollar-of-risk is compressing. This does not necessarily indicate poor underwriting (allowance ratios are improving slightly), but it does indicate the marginal economics of new loan originations are less attractive than the existing book's average.

**Off-balance-sheet exposure:** unused agreed loan commitments on the credit-card portfolio were $9,001M (2025) vs. $2,872M (2024) — a large and rapidly growing contingent exposure.

---

## 6. Debt Schedule

[MELI_10K_FY2025.htm, Note 16]: Total debt of $9,193M (FY2025) vs. $5,715M (FY2024). Key public-market instruments:
- **2026 Sustainability Notes:** $400M original, 2.375% fixed, matured January 14, 2026 (repaid in full; $367M balance at Dec 31, 2025).
- **2031 Notes:** $700M original, 3.125% fixed, matures January 14, 2031; $541M balance at Dec 31, 2025 (some principal repurchased in 2024/2025).
- **2033 Notes:** $750M issued December 9, 2025, 4.900% fixed, matures January 15, 2033; $735M balance at Dec 31, 2025.

The remainder of MELI's debt is a diversified mix of local bank loans (Chilean Pesos, Brazilian Reais CDI-linked, Mexican Pesos TIIE-linked, Uruguayan Pesos), collateralized/securitization debt ($2,852M in FY2025, funding the credit portfolio), Brazilian Financial Bills and Deposit Certificates, and Argentine local-currency instruments carrying very high nominal rates (35.53% fixed on secured credit lines, 34.166% fixed on promissory notes) — a direct reflection of Argentina's high-inflation interest-rate environment.

**2028 Convertible Notes (retired):** $880M of 2.00% Convertible Senior Notes issued August 2018 were "fully converted or redeemed in November 2023" — the associated capped call transactions settled September 1, 2023, meaning MELI's post-2023 share count no longer carries this dilution overhang.

---

## 7. Share Count & Dilution

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Diluted weighted-avg shares (M) | 51.0 | 50.7 | 50.7 |

Share count has been essentially flat-to-slightly-declining since the 2028 convertible notes were retired in November 2023 — MELI does not have a formal buyback program, and dilution from equity compensation has been minimal (only 21 incremental diluted shares from director RSUs in FY2025). Long Term Retention Program (LTRP) stock-based compensation expense: $303M (FY2025), $261M (FY2024), $167M (FY2023) — a real and growing non-cash expense, though not translating into meaningful share-count dilution to date.

---

## 8. Impairments, One-Time Items, and Hyperinflation Mechanics

- **No goodwill impairment.** [MELI_10K_FY2025.htm]: "the Company performed its annual goodwill impairment analysis... concluded that it was more likely than not that the fair value of each reporting unit... exceeds its carrying value." Goodwill grew from $149M (2024) to $163M (2025), entirely via currency translation (no FY2025 acquisitions).
- **No long-lived asset impairment.** [MELI_10K_FY2025.htm]: "there were no events or changes in circumstances that indicate that the carrying value of an asset may not be recoverable."
- **No restructuring charges disclosed** in any of the three filings reviewed.
- **Minor impairment of equity securities held at cost:** $19M (FY2025), $0 (FY2024/FY2023).
- **Foreign currency losses, net:** $(615)M (FY2023) — coinciding with Argentina's 211.4% inflation and 356.3% currency depreciation that year — versus much smaller losses of $(182)M (FY2024) and $(337)M (FY2025) as Argentine currency volatility moderated. This line item is the primary place Argentina's macro volatility shows up in MELI's consolidated income statement.

Not found in available filings: a separately labeled "monetary position gain/loss" line (not applicable, since MELI uses the USD-functional-currency approach for Argentina rather than IAS 29-style price-level restatement); a board-authorized share repurchase program.
