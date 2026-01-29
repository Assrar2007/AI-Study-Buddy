from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import time
import os

def export_to_pdf(summary, explanation, flashcards, mcq, chatbot, filename="study_material.pdf"):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_file = f"exported_{timestamp}.pdf"

    c = canvas.Canvas(output_file, pagesize=LETTER)
    width, height = LETTER

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "AI Study Buddy Output")

    y = height - 100
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Summary:")
    y -= 20
    c.setFont("Helvetica", 11)
    for line in summary.split("\n"):
        c.drawString(50, y, line)
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Explanation:")
    y -= 20
    c.setFont("Helvetica", 11)
    for line in explanation.split("\n"):
        c.drawString(50, y, line)
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Flashcards:")
    y -= 20
    c.setFont("Helvetica", 11)
    for line in flashcards.split("\n"):
        c.drawString(50, y, line)
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "MCQs:")
    y -= 20
    c.setFont("Helvetica", 11)
    for line in mcq.split("\n"):
        c.drawString(50, y, line)
        y -= 15

    c.showPage()
    c.save()

    return output_file