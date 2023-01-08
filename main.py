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

    invoice_nr, date = filename.split("-")
    invoice_nr = "Invoice nr. " + invoice_nr
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=0, h=8, txt=invoice_nr, ln=1, align="L")

    date = "Date: " + date
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=0, h=8, txt=date, ln=1, align="L")

    columns = list(df.columns)
    columns_header = [item.replace("_", " ").title() for item in columns]

    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_fill_color(200, 200, 200)

    pdf.cell(w=30, h=6, txt=columns_header[0], fill=True, border=1)
    pdf.cell(w=73, h=6, txt=columns_header[1], fill=True, border=1)
    pdf.cell(w=32, h=6, txt=columns_header[2], fill=True, border=1)
    pdf.cell(w=30, h=6, txt=columns_header[3], fill=True, border=1)
    pdf.cell(w=30, h=6, txt=columns_header[4], fill=True, border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=30, h=6, txt=str(row[columns[0]]), border=1)
        pdf.cell(w=73, h=6, txt=row[columns[1]], border=1)
        pdf.cell(w=32, h=6, txt=str(row[columns[2]]), border=1)
        pdf.cell(w=30, h=6, txt=str(row[columns[3]]), border=1)
        pdf.cell(w=30, h=6, txt=str(row[columns[4]]), border=1, ln=1)

    total_sum = str(df[columns[4]].sum())
    pdf.cell(w=30, h=6, txt="", border=1)
    pdf.cell(w=73, h=6, txt="", border=1)
    pdf.cell(w=32, h=6, txt="", border=1)
    pdf.cell(w=30, h=6, txt="", border=1)
    pdf.cell(w=30, h=6, txt=total_sum, fill=True, border=1, ln=1)

    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=45, h=12, txt="RandomCompanyName")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"pdfs/{filename}.pdf")
