import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr = "Invoice nr. " + filename.split("-")[0]

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=0, h=12, txt=invoice_nr, ln=12, align="L")
    pdf.output(f"pdfs/{filename}.pdf")

