# Broadcom Inc. (AVGO) — Valuation Check

*Analysis date: 2026-04-08 | Sources: FY2025 10-K, external market data (StockAnalysis, Yahoo Finance, GuruFocus)*
*Note: This is a sanity check, not a precise model. All market data is as of ~April 7-8, 2026.*

---

## 1. Relative Valuation

### Current multiples

| Multiple | AVGO Current | Basis |
|---|---|---|
| **Trailing P/E** | ~65x | TTM GAAP EPS ~$5.13 |
| **Forward P/E** | ~25x | FY2026 consensus GAAP EPS ~$11.50 |
| **EV/EBITDA** | ~46x | EV ~$1.72T / TTM EBITDA |
| **P/FCF** | ~58x | Market cap ~$1.66T / TTM FCF ~$26.9B |
| **PEG** | ~0.60 | Forward P/E / consensus growth rate |
| **FCF Yield** | ~1.7% | Inverse of P/FCF |

*(Note: all market multiples from StockAnalysis, Yahoo Finance, GuruFocus — not from uploaded filings)*

### vs. Own 5-year historical average

| Multiple | Current | 5-Yr Avg (FY2021-25) | Avg ex-FY2024 | Current vs. Avg |
|---|---|---|---|---|
| Trailing P/E | ~65x | ~58.7x | ~39x | At avg (or +67% vs. ex-FY2024 avg) |
| EV/EBITDA | ~46x | ~27.2x | ~15.7x | +69% premium (or +193% vs. ex-FY2024) |
| P/FCF | ~58x | ~30.8x | ~16.1x | +88% premium |

The 5-year averages are heavily skewed by FY2024 (137x P/E due to VMware acquisition charges). Excluding FY2024, AVGO historically traded at ~39x P/E and ~16x EV/EBITDA — meaning current multiples represent a significant re-rating.

### vs. Peer group (April 2026)

| Company | Mkt Cap | Trail P/E | Fwd P/E | EV/EBITDA | PEG |
|---|---|---|---|---|---|
| **AVGO** | **$1.66T** | **65x** | **25x** | **46x** | **0.60** |
| NVDA | $4.42T | 36x | 21x | 33x | 0.56 |
| MRVL | $100B | 37x | 30x | 39x | 0.75 |
| QCOM | $136B | 25x | 12x | 10x | 2.64 |
| TXN | $190B | 38x | 32x | 25x | 2.13 |
| NTNX | $10.5B | 43x | 20x | 35x | 1.86 |

**Key observations:**
- AVGO trades at the **highest trailing P/E** in the peer group (65x vs. NVDA's 36x), driven by GAAP earnings still depressed by VMware amortization
- On a **forward P/E** basis (25x), AVGO is broadly in line with NVDA (21x) and MRVL (30x) — the market expects rapid earnings normalization
- AVGO's **PEG of 0.60** is the lowest in the group alongside NVDA (0.56), suggesting it is not obviously overvalued relative to expected growth
- **QCOM at 12x forward P/E** represents the "value" end of the semiconductor spectrum — AVGO commands a 2x premium

### vs. Semiconductor sector median

| | AVGO | Sector Median (156 cos.) | Premium |
|---|---|---|---|
| Trailing P/E | ~65x | ~33x | ~97% |
| EV/EBITDA | ~46x | ~23x | ~100% |

AVGO trades at roughly **2x the semiconductor sector median** on both P/E and EV/EBITDA. This premium is justified only if growth and margin trajectory significantly exceed the sector average.

---

## 2. Growth-Adjusted View

### PEG ratio

| | PEG | Interpretation |
|---|---|---|
| AVGO | 0.60 | Attractive (below 1.0) |
| NVDA | 0.56 | Attractive |
| MRVL | 0.75 | Attractive |
| QCOM | 2.64 | Expensive relative to growth |
| TXN | 2.13 | Expensive relative to growth |

A PEG of 0.60 implies the market is pricing in ~42% annual earnings growth (forward P/E of 25 / PEG of 0.60), which aligns with consensus estimates: FY2026 GAAP EPS of ~$11.50 vs. FY2025's $4.77 = +141% growth.

**Caveat:** The PEG looks attractive because the growth rate is extremely high — but this growth is partly an accounting artifact (FY2025 GAAP earnings were depressed by VMware charges and a -1.7% tax rate). Normalized growth rates will be significantly lower once the VMware integration anniversary completes.

### EV/EBITDA-to-growth

Consensus FY2026 revenue growth: ~67% ($63.9B → ~$106.6B). Not found in available data: consensus EBITDA estimate for FY2026. However, if EBITDA grows proportionally, EV/EBITDA-to-growth ≈ 46 / 67 ≈ 0.7x — also below 1.0 and superficially attractive.

**Caveat:** The ~67% revenue growth includes full-year AI scaling and VMware anniversary effects. Sustainable long-term revenue growth is likely in the 15-25% range, which would imply a significantly less attractive growth-adjusted valuation.

---

## 3. Simple Intrinsic Value — Reverse DCF

### What growth rate is the current price implying?

**Assumptions:**
- Current market cap: ~$1.66T
- FY2025 FCF: $26.9B (reported)
- Terminal growth rate: 3%
- Discount rate (WACC): 10%
- Projection period: 10 years

**Reverse DCF result:** To justify a $1.66T market cap, FCF must grow at approximately **18-20% annually** for the next 10 years (reaching ~$130-150B in FCF by FY2035), then grow at 3% in perpetuity.

**Is this reasonable?**

| Scenario | Required 10-yr FCF CAGR | FY2035 FCF | Plausibility |
|---|---|---|---|
| Current price implied | ~18-20% | ~$130-150B | Ambitious but not impossible |
| Historical (FY2021-25 CAGR) | ~19% | In range | Consistent — but included VMware step-change |
| Organic only (no M&A) | ~12-15% | ~$85-115B | More realistic for a $64B revenue company |

The implied growth rate is achievable if: (a) AI semiconductor spending continues at 15-20% CAGR, (b) VMware subscription revenue grows at 10-15%, and (c) Broadcom maintains 40%+ FCF margins. It is aggressive but not unreasonable given the current trajectory.

**However:** FCF of $26.9B includes $7.6B of SBC added back. If SBC-adjusted FCF ($19.3B) is used as the base, the implied growth rate rises to **~23-25%** — significantly more demanding.

---

## 4. Margin of Safety

### What needs to go right (already priced in)

- AI semiconductor revenue continues growing 20%+ annually through FY2030
- VMware VCF renewal rates remain high (>90% of top customers)
- Software margins stay above 70%
- No major hyperscaler in-sources custom silicon away from Broadcom
- Tax rate normalizes to ~15% (not higher)
- Hock Tan remains at the helm through FY2030
- No Taiwan Strait disruption to TSMC supply

### What is NOT priced in (potential upside)

- Additional large acquisitions that expand the software franchise
- AI networking TAM exceeds current estimates ($60-90B by 2027)
- Broadcom captures networking share from NVIDIA's InfiniBand in AI clusters
- Global minimum tax implementation is less severe than feared
- Share count declines meaningfully through buybacks

### What is NOT priced in (potential downside)

- AI capex cycle peaks and declines (semiconductor cyclicality reasserts)
- VMware customer defections accelerate (Gartner: market share could drop to 40% by 2029)
- Export controls expand to restrict more of Broadcom's China revenue ($11.2B at risk)
- AR factoring facilities are tightened, forcing $7.4B onto the balance sheet
- Contract liabilities continue declining (signaling booking slowdown)

### Margin of safety assessment

At ~65x trailing earnings and ~25x forward earnings, the stock **has limited margin of safety**. The FCF yield of 1.7% is well below the 10-year median of ~5.5%. The valuation requires sustained execution across all growth vectors simultaneously. Any single thesis pillar breaking (AI capex slowdown, VMware churn, customer concentration event) could compress multiples by 30-50%.

---

## 5. Scenario Framing

All scenarios use FY2027 as the terminal year for valuation. Shares outstanding assumed at ~4.8B.

### Bull Case (top-quartile outcome)

**Assumptions:**
- FY2027 revenue reaches $160B+ (consensus: $163B)
- AI semiconductor revenue exceeds $100B (per management guidance)
- Software margins reach 80%+
- Consolidated FCF margin stays at 40%+
- Multiple: 30x forward P/E (AI premium sustained)

| Metric | Bull Value |
|---|---|
| FY2027 EPS (GAAP) | ~$18 |
| Multiple | 30x forward |
| **Fair Value** | **~$540/share** |
| Implied upside | ~55% from ~$350 |

### Base Case (continuation of current trends)

**Assumptions:**
- FY2027 revenue of ~$130-140B (below consensus; accounts for some AI cooling)
- Software retention holds but growth moderates to ~15%
- FCF margin compresses modestly to 37% (SBC and taxes normalize)
- Multiple: 25x forward P/E (slight re-rating down as growth slows)

| Metric | Base Value |
|---|---|
| FY2027 EPS (GAAP) | ~$13-14 |
| Multiple | 25x forward |
| **Fair Value** | **~$325-350/share** |
| Implied return | Roughly flat from ~$350 |

### Bear Case (structural deterioration)

**Assumptions:**
- AI capex cycle peaks in FY2026; semiconductor revenue declines 10-15% in FY2027
- VMware loses 15-20% of mid-market customers to Nutanix/Red Hat
- Tax rate normalizes to 18%+ (global minimum tax)
- Single largest customer reduces orders by 20%
- Multiple: 18x forward P/E (de-rating to semi-sector average)

| Metric | Bear Value |
|---|---|
| FY2027 EPS (GAAP) | ~$8-9 |
| Multiple | 18x forward |
| **Fair Value** | **~$145-160/share** |
| Implied downside | ~55% from ~$350 |

### Scenario summary

| Scenario | FY2027 EPS | Multiple | Fair Value | Return |
|---|---|---|---|---|
| **Bull** | ~$18 | 30x | **~$540** | +55% |
| **Base** | ~$13-14 | 25x | **~$325-350** | ~Flat |
| **Bear** | ~$8-9 | 18x | **~$145-160** | -55% |

The risk/reward is roughly symmetric at current prices: ~55% upside in the bull case vs. ~55% downside in the bear case, with the base case suggesting the stock is approximately fairly valued.

---

## Key Caveats

1. **GAAP vs. Non-GAAP:** All EPS figures above are GAAP. Broadcom's non-GAAP EPS (excluding acquisition amortization and SBC) is materially higher. Many analysts value the stock on non-GAAP earnings, which makes it appear cheaper.

2. **FY2026 consensus revenue of $107B implies +67% growth** — extraordinarily high and reliant on AI revenue scaling. If this is achieved, the forward P/E will compress rapidly from 25x to a lower normalized level.

3. **The VMware amortization distortion will persist** for several more years ($8B+/year), keeping GAAP earnings well below economic reality. Segment operating margins (57.6% semi, 76.8% software) are a better gauge of true profitability.

4. **This analysis does not account for potential future M&A**, which has been Broadcom's primary value creation mechanism historically.

5. **All external market data** (prices, multiples, consensus estimates) from StockAnalysis, Yahoo Finance, GuruFocus — not from uploaded SEC filings.
