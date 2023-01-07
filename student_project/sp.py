import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("txts/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filename = Path(filepath).stem.capitalize()

    pdf.add_page()

    pdf.set_font("Times", "B", 16)
    pdf.cell(20, 10, txt=filename, ln=16)

pdf.output("output.pdf")
