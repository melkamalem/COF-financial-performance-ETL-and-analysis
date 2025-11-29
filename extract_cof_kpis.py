import pdfplumber, pandas as pd, re

PDF_PATH = "Q4_2024_Earnings_Release.pdf"

def extract_first_n_numbers(text, n=5):
    """Return first n numeric values (as floats) from a text row."""
    tokens = re.findall(r"\(?-?\d[\d,]*\)?", str(text))
    values = []
    for t in tokens:
        neg = t.startswith("(") and t.endswith(")")
        s = t.strip("()").replace(",", "")
        try:
            v = float(s)
            if neg:
                v = -v
            values.append(v)
        except ValueError:
            continue
    return values[:n]

with pdfplumber.open(PDF_PATH) as pdf:
    income_page = pdf.pages[1]          
    income_tbl = income_page.extract_tables()[0]
    income_df = pd.DataFrame(income_tbl[1:], columns=income_tbl[0])

    balance_page = pdf.pages[2]         
    balance_tbl = balance_page.extract_tables()[0]
    balance_df = pd.DataFrame(balance_tbl[1:], columns=balance_tbl[0])

net_interest_row = income_df.iloc[0, 0]      
noninterest_row = income_df.iloc[1, 0]      
noninterest_exp_row = income_df.iloc[7, 0]   
loans_row = balance_df.iloc[0, 0]           

interest = extract_first_n_numbers(net_interest_row)
noninterest = extract_first_n_numbers(noninterest_row)
noninterest_exp = extract_first_n_numbers(noninterest_exp_row)
loans = extract_first_n_numbers(loans_row)

quarters = ["2024-Q4", "2024-Q3", "2024-Q2", "2024-Q1", "2023-Q4"]

df = pd.DataFrame({
    "quarter": quarters,
    "interest_income": interest,
    "noninterest_income": noninterest,
    "noninterest_expense": noninterest_exp,
    "loan_balance": loans,
})

df.to_csv("cof_quarterly_kpis.csv", index=False)
print(df)
print("\nSaved → cof_quarterly_kpis.csv")
