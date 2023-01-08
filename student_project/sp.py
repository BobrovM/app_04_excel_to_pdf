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

    with open(filepath, "r") as file:
        content = file.read()

    #file = open(filepath)
    #content = file.read()
    #file.close()

    pdf.set_font("Times", size=12)
    pdf.multi_cell(w=0, h=8, txt=content)

pdf.output("output.pdf")
