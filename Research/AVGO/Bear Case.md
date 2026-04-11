# Broadcom Inc. (AVGO) — Bear Case

*Analysis date: 2026-04-08 | Sources: FY2025, FY2024, FY2023 10-Ks*
*Perspective: Short thesis for skeptical investor committee*

---

## 1. Thesis Killer: Customer Concentration in a Cyclical AI Capex Boom

The single most likely way a long-term AVGO holder loses money is a **pullback in AI infrastructure spending by Broadcom's hyperscaler customers**.

One unnamed semiconductor customer — widely understood to be a major distributor serving a hyperscaler — now accounts for **32% of total revenue** and **44% of accounts receivable**.

[AVGO_10K_FY2025.htm, Segment Note]:
> "During fiscal years 2025, 2024 and 2023, one customer accounted for 32%, 28% and 21% of our net revenue, respectively."

This concentration has been **accelerating**, not stabilizing (21% → 28% → 32% in three years). The top 5 end customers represent ~40% of revenue.

Meanwhile, Broadcom's own filing warns the AI boom may not be durable:

[AVGO_10K_FY2025.htm, Risk Factors]:
> "The semiconductor industry is undergoing profound change due to the adoption and proliferation of AI and has experienced a significant upturn, which may not be sustainable. [...] Some of these AI customers may have constrained resources or capital and may be unable to pay for their required AI infrastructure."

Broadcom has begun offering **deferred payment models and equipment leasing** for AI racks — a tacit acknowledgment that some AI customers cannot pay upfront. This is a late-cycle signal: extending credit to drive growth.

**The math on a pullback:** If the top customer reduces orders by 30% (a moderate capex correction), Broadcom loses ~$6.5B in revenue (~10% of total) with near-immediate margin impact given the operating leverage in semiconductors.

---

## 2. Structural Weaknesses

### 2a. VMware customer defection risk

Broadcom's aggressive pricing and bundling strategy for VMware has driven measurable customer migration to alternatives. External industry data suggests VMware's hypervisor market share may decline from ~72% (2024) to ~40% by 2029 (Gartner estimate — not from uploaded filings). Broadcom's own filing does not disclose customer churn metrics.

The subscription conversion is a double-edged sword: 67% of contract liabilities have termination-for-convenience clauses, meaning customers can walk away.

[AVGO_10K_FY2025.htm, Revenue Recognition]:
> "For software arrangements with termination for convenience provisions, we account for these arrangements as a series of daily contracts."

If enterprise customers migrate to Nutanix, Red Hat, or public cloud alternatives faster than expected, the $27B software revenue base could erode rather than grow.

### 2b. Fabless model = zero manufacturing control

[AVGO_10K_FY2025.htm, Risk Factors]:
> "During fiscal year 2025, approximately 95% of the wafers manufactured by our CMs were produced by TSMC."

95% dependence on a single foundry located in **Taiwan** — amid escalating U.S.-China tensions over Taiwan — is an existential supply chain risk. Broadcom has **no long-term supply contracts**:

[AVGO_10K_FY2025.htm, Risk Factors]:
> "We do not generally have long-term capacity commitments with our CMs and substantially all of our manufacturing services are on a purchase order basis with no minimum quantities."

A Taiwan Strait crisis, even a limited one, would halt 95% of Broadcom's wafer supply.

### 2c. Broadband and storage are secularly declining

While AI networking is growing, Broadcom's broadband (set-top box SoCs, DSL/cable modems) and legacy storage (HDD controllers, SAS/RAID) product lines face **secular headwinds**:
- Streaming is replacing set-top boxes
- SSDs are replacing HDDs
- Cloud is replacing on-premises storage arrays

These product lines will require progressively higher AI revenue just to keep overall growth positive.

---

## 3. Assumptions the Bull Case Takes for Granted

### 3a. AI capex grows indefinitely

The bull case assumes hyperscaler AI infrastructure spending continues at 20%+ growth rates. But the semiconductor industry has experienced **13+ downturns since 1963**, averaging one every 4-4.5 years. The current AI upcycle began in early 2023 — we are now 3+ years in.

### 3b. Custom silicon stays outsourced

Broadcom's XPU business depends on hyperscalers **choosing to outsource** custom chip design rather than build internal teams. Google already has TPUs designed in-house. If more hyperscalers follow, Broadcom's custom silicon TAM could shrink.

[AVGO_10K_FY2025.htm, Risk Factors]:
> "We also expect competition in these markets to continue to increase as [...] new companies, including some of our customers, enter the markets."

### 3c. VMware retention holds at current levels

The bull case assumes 87% of top VMware customers stay. But subscription conversions are still early, and each renewal cycle is an off-ramp opportunity for customers who've spent the last 2 years evaluating alternatives.

### 3d. SBC is manageable

SBC at 11.8% of revenue ($7.6B) is treated as a non-cash item by FCF-focused bulls. But it's **real dilution**: shares outstanding grew from 4,272M (FY2023) to 4,853M (FY2025) — a 14% increase in two years. At current share prices, this is tens of billions in economic cost.

### 3e. Tax rates stay low

Broadcom's FY2025 effective tax rate was -1.7% (a benefit). Cash taxes paid were $2.6B (~4% of pre-tax income). Management explicitly warns this will change:

[AVGO_10K_FY2025.htm, Risk Factors]:
> "We are in the process of implementing a global minimum tax, which we expect to materially increase our effective tax rate and cash tax costs for our fiscal year ending November 1, 2026."

A normalization to even a 15% cash tax rate would reduce FCF by ~$1-2B annually.

---

## 4. Permanent Impairment Scenarios

### 4a. Taiwan crisis

A Chinese blockade or invasion of Taiwan would halt TSMC production, eliminating 95% of Broadcom's wafer supply. Even a 6-month disruption would devastate revenue, trigger customer defections to competitors with alternative supply chains, and potentially impair the franchise permanently. TSMC's Arizona fabs are not yet at scale for Broadcom's advanced node requirements.

### 4b. Hyperscaler vertical integration in networking

If Google, Amazon, Microsoft, and Meta all develop their own Ethernet switching silicon (as some are already doing with compute accelerators), Broadcom's networking franchise — the growth engine of the semiconductor segment — could face structural displacement. This would not happen overnight but could erode the TAM over 5-10 years.

### 4c. VMware open-source displacement

If the private cloud market shifts decisively toward open-source alternatives (KVM/Proxmox) or public cloud fully absorbs the workloads VMware serves, the $27B software segment could face permanent revenue decline. The 76.8% margin makes even modest revenue declines devastating to absolute profit.

### 4d. Goodwill impairment

$97.8B in goodwill (57% of total assets) creates latent impairment risk. If the software segment's earning power deteriorates (e.g., VMware churn exceeds expectations), Broadcom would need to write down goodwill — potentially tens of billions of dollars.

[AVGO_10K_FY2025.htm, Balance Sheet]:
> "Goodwill $97,801M"

At 57% of assets, even a 20% impairment ($19.6B) would eliminate nearly one quarter of stockholders' equity.

---

## 5. Hidden Balance Sheet Risks

### 5a. Off-balance-sheet purchase commitments

Not found in available filings: specific quantification of non-cancelable purchase commitments. However, the filing notes dependence on purchase orders with no long-term commitments — meaning Broadcom also lacks guaranteed supply, creating asymmetric risk.

### 5b. AR factoring masks true receivables exposure

[AVGO_10K_FY2025.htm, Note — Accounts Receivable Factoring]:
> "Total trade accounts receivable sold under the factoring arrangements were $7,401 million, $5,900 million and $3,975 million during fiscal years 2025, 2024 and 2023, respectively."

Broadcom sold $7.4B in receivables off-balance-sheet in FY2025. Adding this back, true gross AR is ~$14.5B — not the $7.1B reported. True DSO is ~83 days, not 40.8. The factoring program has grown 86% in two years, and if factoring facilities were withdrawn (e.g., during a credit crunch), Broadcom would need to absorb ~$7.4B in additional working capital on its balance sheet.

### 5c. Deferred payment / AI leasing risk

[AVGO_10K_FY2025.htm, Risk Factors]:
> "We may offer and have offered alternative financings or other novel or deferred payment models for the leasing of AI racks or systems based on our XPUs [...] which could have a material adverse effect on our revenue, free cash flow and gross margin and expose us to credit or customer default risks."

This is a new and explicitly disclosed risk: Broadcom is effectively financing customer purchases, adding **credit risk** to the balance sheet that didn't exist pre-AI boom.

### 5c. Acquisition-related contingent liabilities

$97.8B in goodwill and $32.3B in intangible assets represent $130.1B in acquisition-related assets — 76% of the balance sheet. Any deterioration in the acquired businesses' performance could trigger impairment testing and write-downs.

### 5d. Tax contingencies

[AVGO_10K_FY2025.htm, Tax Note]:
The FY2024 tax provision included a massive one-time charge related to IP restructuring. Broadcom operates complex international tax structures. The implementation of global minimum tax (Pillar Two) will increase cash taxes. The CAMT credit valuation allowance of $1,321M already signals the tax landscape is shifting against Broadcom.

### 5e. Operating lease obligations

[AVGO_10K_FY2025.htm, Lease Note]:
Total undiscounted operating lease liabilities: $1,725M. This is modest relative to the business scale but represents a fixed cost commitment.

---

## 6. Management Risk

### 6a. Key-person dependence: Hock Tan

[AVGO_10K_FY2025.htm, Risk Factors]:
> "We are dependent on senior management and if we are unable to attract and retain qualified personnel, we may not be able to execute our business strategy effectively."

Hock Tan has been the architect of Broadcom's acquisition strategy since 2006. The company's track record of acquiring, cost-cutting, and integrating is largely attributed to his discipline. A sudden departure — for health, regulatory, or personal reasons — would create material uncertainty. No obvious internal successor has been publicly identified.

### 6b. Empire-building through M&A

Broadcom's entire growth strategy is M&A-driven. The balance sheet reflects this: $130B in goodwill + intangibles on $63.9B in revenue. Each acquisition adds leverage and integration risk. The VMware acquisition has worked so far, but the next large deal could destroy value — as Broadcom's own attempt to acquire Qualcomm in 2018 (blocked by the U.S. government) would have required ~$140B in capital.

### 6c. SBC as a wealth transfer

$7.6B in SBC (11.8% of revenue) in FY2025 — more than doubled from $2.2B (6.1%) in FY2023. This represents a wealth transfer from existing shareholders to employees. Shares outstanding have grown 14% in two years. At a ~$200 stock price, that's roughly $25B in economic value transferred to employees in 2 years.

---

## 7. What Would Prove the Bear Right

Specific, observable triggers:

| Trigger | Current Level | Bear Signal |
|---|---|---|
| **Top customer revenue share** | 32% | Declines below 25% (customer diversifying away) OR exceeds 40% (dangerous over-dependence) |
| **Semiconductor segment YoY growth** | +22% | Turns negative for 2+ consecutive quarters |
| **Software segment operating margin** | 76.8% | Falls below 65% for 2+ quarters (indicating pricing/retention issues) |
| **Net debt / EBITDA** | 1.5x | Rises above 2.5x (re-leveraging for acquisitions) |
| **DSO** | 40.8 days | Exceeds 50 days (collection problems, extended terms) |
| **SBC as % of revenue** | 11.8% | Exceeds 15% (excessive dilution) |
| **China revenue** | $11.2B (17.5%) | Drops below $8B (export controls biting) OR spikes (re-routing risk) |
| **VMware contract liabilities** | ~$15B | Declines QoQ for 2+ quarters (customers not renewing) |
| **TSMC wafer concentration** | 95% | Unchanged at 95%+ despite stated diversification goals |
| **Goodwill impairment** | $0 | Any impairment charge signals fundamental business deterioration |
| **Cash tax rate** | ~4% | Normalizes to 15%+ per global minimum tax, reducing FCF by $1-2B/year |

---

## Summary

The short thesis is straightforward: **Broadcom is a $64B-revenue company where 32% of revenue comes from one customer, 95% of manufacturing depends on one foundry, and 57% of assets are goodwill from acquisitions — all at a time when the AI capex cycle that drives its growth engine is 3+ years old and its own filing warns "may not be sustainable."**

The company is exceptionally well-managed and the current financial performance is extraordinary. But the bear case is not about today's performance — it's about the **fragility of the conditions that produce it**. Customer concentration, supply chain concentration, and acquisition-dependent growth create a business that is more brittle than its margins suggest. When (not if) AI capex cycles, the downside for a 32%-single-customer business will be severe.
