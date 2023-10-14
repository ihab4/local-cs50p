from fpdf import FPDF, Align


# name = input("Name: ").title()
name = "John Harvard"

from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        pdf.set_font("Times", size=36)
        pdf.ln(10)
        pdf.cell(txt="CS50 Shirtificate", align="X", center=True)
        self.ln(20)

pdf = PDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font("Times", size=36)
pdf.image("shirtificate.png", x=Align.C, y=35)
pdf.ln(60)
pdf.set_text_color(255, 255, 255)
pdf.cell(txt=f"{name} took CS50", align="X", center=True)
pdf.output("shirtificate.pdf")