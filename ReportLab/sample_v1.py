from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
# import django

c = canvas.Canvas("Hello World")
c.drawString(9*cm, 22*cm, "Hello World!")
c.showPage()
c.save()
