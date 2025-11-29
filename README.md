# Banking Financial Performance & KPI ETL Pipeline (Capital One – SEC-Based)

This project builds a **lightweight, production-style ETL pipeline** that extracts key financial KPIs from Capital One’s quarterly financial supplement (Q4 2024), cleans the data, structures it into a unified dataset, and performs **quarter-over-quarter performance analysis** across the 5 most recent quarters (2023-Q4 → 2024-Q4).

The pipeline is intentionally minimalist (~40 total lines of Python) to demonstrate:
- Practical ETL design
- KPI extraction from messy real-world financial sources (PDFs)
- Data cleaning & numerical standardization
- Period-over-period analysis
- Business-ready insights relevant to banking & credit institutions

---

## **KPIs Included & Why These Four Matter Most**
This project focuses on four of the **most fundamental, universal, and decision-driving metrics** for evaluating the financial performance of any large retail bank:

### **1. Net Interest Income (NII)**
NII is the **core driver of banking profitability**.  
It reflects the spread between interest earned on loans and interest paid on deposits and borrowings.

Why it matters:
- Primary revenue source for credit-card and consumer-lending banks  
- Moves with rate cycles (Fed policy), loan growth, and deposit costs  
- First indicator of margin compression or expansion (NIM trends)

### **2. Noninterest Income**
Represents **fee-based revenue** from services such as:
- interchange fees (credit card purchases)
- service charges
- investment products
- other revenue streams not tied to lending

Why it matters:
- Diversifies revenue beyond interest rate movements  
- Helps determine the health of consumer activity (e.g., card spending)  
- Critical for assessing business resilience

### **3. Noninterest Expense**
Includes:
- compensation  
- marketing  
- operations  
- fraud/processing  
- technology spend  

Why it matters:
- Direct measure of operational efficiency  
- Affected by investment cycles, tech modernization, and credit operations  
- Determines how effectively the bank converts revenue into profit  
- A key input to the **Efficiency Ratio** (a core bank profitability metric)

### **4. Loans Held for Investment (HFI)**
Total loan balances are one of the bank’s largest earning assets.
- Drives interest income  
- Moves with credit demand and underwriting strategy  
- Indicates portfolio growth or tightening  
- Linked to credit quality, capital, and risk appetite

---

## **Why These Four KPIs Were Chosen**
These KPIs were selected because they represent the **cleanest, most interpretable**, and **most business-essential** indicators for:

- Profitability  
- Operational efficiency  
- Core revenue drivers  
- Balance sheet strength  

They are also:
- available consistently in every quarter’s supplement  
- comparable across periods  
- standard across the banking industry  
- directly tied to investor reporting and analyst calls  

In short:

> **If you can explain these four KPIs clearly, you can explain 80% of a bank’s financial performance.**

That is why this project prioritizes these metrics despite the availability of dozens of additional measures in the filings.

---

## **Project Workflow**
1. **PDF ingestion** using `pdfplumber`  
2. **Table extraction** across all pages  
3. **Pattern matching** to locate the KPI rows  
4. **Cleaning & normalization** of financial data  
5. **Quarter label standardization**  
6. **Construction of a structured DataFrame** (5 quarters of KPIs)  
7. **Quarter-over-quarter performance calculations**  
8. **Visualization and insights**

---

## **Quarter-over-Quarter Performance Analysis (Q4 2023 → Q4 2024)**

The notebook generates:
- 5-quarter trendline charts  
- QoQ deltas for all KPIs  
- Performance commentary explaining:
  - revenue stability or compression  
  - efficiency movements  
  - expense pressures  
  - credit portfolio growth  
  - macro-sensitive changes  

Insights are inspired by institutional-grade financial analysis but remain concise and business-friendly.

---

## **Files in This Repository**
- `extract_cof_kpis.py` → PDF ETL script  
- `banking_kpi_analysis.ipynb` → Final analysis notebook  
- `cof_quarterly_kpis.csv` → Cleaned KPI dataset  
- `README.md` → Project documentation  
