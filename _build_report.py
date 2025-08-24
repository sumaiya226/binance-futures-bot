from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def build_report(path: str = "report.pdf"):
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4
    t = c.beginText(2*cm, height - 2*cm)
    t.setFont("Helvetica-Bold", 16)
    t.textLine("Binance USDT-M Futures Order Bot — Report")
    t.setFont("Helvetica", 11)
    t.textLine("")
    t.textLines(
        "This report summarizes the bot features and how to test on Binance Futures Testnet.\n"
        "- Core Orders: Market, Limit\n"
        "- Advanced: Stop-Limit, OCO (simulated), TWAP, Grid\n"
        "- Logging: bot.log\n"
        "- Setup: see README.md\n"
        "\nScreenshots: add your terminal screenshots here after running sample commands."
    )
    c.drawText(t)
    c.showPage()
    c.save()
