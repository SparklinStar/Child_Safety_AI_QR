from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os


def create_student_pdf(data_dict, photo_filename, pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Draw boundary lines
    margin = 50
    page_width, page_height = letter
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)  # Set line width to 1 point
    c.rect(margin, margin, page_width - 2 * margin, page_height - 2 * margin)

    # Calculate image position
    image_width = 100
    image_height = 100
    x_pos = page_width - margin - image_width - 10
    y_pos = page_height - margin - image_height - 10

    # Add image inside the boundary
    photo = Image.open(photo_filename)
    print('Inside create' ,photo_filename )
    c.drawImage(photo_filename, x_pos, y_pos, width=image_width, height=image_height)

    # Set font and size for titles and content
    title_font = "Helvetica-Bold"
    content_font = "Helvetica"
    font_size = 12

    # Add content
    text_margin = margin + 20
    text_y = page_height - margin - 50

    for title, content in data_dict.items():
        c.setFont(title_font, font_size)
        
        # Split "Last Four Digits of Adhaar" title into two lines
        if title == "Last Four Digits of Adhaar":
            title_lines = title.split(" ")
            c.drawString(text_margin, text_y, title_lines[0])
            c.drawString(text_margin, text_y - 20, title_lines[1] + ":")
        else:
            c.drawString(text_margin, text_y, title + ":")
        
        c.setFont(content_font, font_size)
        c.drawString(text_margin + 120, text_y, content)
        
        text_y -= 20

    # Save the canvas
    c.save()
