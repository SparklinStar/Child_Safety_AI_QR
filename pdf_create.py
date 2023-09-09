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

def create_qr_code_pdf(Name,Birthday, FathersName,MothersName,Address,Gender,Contact,anothercontact,Contact_Email,SchoolName,SchoolAddress,city,state,ZipCode,Country,Blood_Group,Identification_mark,Allergenes):
        
        data_dict = {
            "Name": str(Name),
            "Date of Birth": str(Birthday),
            "Address": str(Address),
            "Father's Name": str(FathersName),
            "Mother's Name": str(MothersName),
            "Gender": str(Gender),
            "Contact No.": str(Contact),
            "Another Contact No.": str(anothercontact),
            "Contact Email": str(Contact_Email),
            "School": str(SchoolName),
            "School Location": str(SchoolAddress),
            "City": str(city),
            
            "State": str(state),
            "Country": str(Country),
            "Zip Code": str(ZipCode),
            "Blood Group":  str(Blood_Group),
            "Identification Mark": str(Identification_mark),
            "Allergen": str(Allergenes),
        }


        photo_filename = "uploaded_image.png" # Provide the path to the student's photo
        pdf_filename = "student_information_boundary_and_image.pdf"
        print('photo_filename',photo_filename)

        create_student_pdf(data_dict, photo_filename, pdf_filename)
        file = print(f"PDF created: {pdf_filename}")
        
        pdf_file_path = "student_information_boundary_and_image.pdf" 
        #file_URL = os.system("curl -F'file=@student_information_boundary_and_image.pdf' https://ttm.sh")
        #print(file_URL)         
        # Construct the curl command
        #curl_command = f"curl -F'file=@{pdf_file_path}' https://ttm.sh"
        curl_command = f'curl -X POST --data-binary "@{pdf_file_path}" --header "Content-Type: application/pdf" "https://www.filestackapi.com/api/store/S3?key=A2KEL5NMLSdiWJ2LMJP20z"'
        # Run the curl command and capture the output
        file_URL = os.popen(curl_command).read().strip()
        file_URL = file_URL.split('"')[3]
        print("Uploaded file URL:", str(file_URL))
        print(file)
        print(file_URL)
        return str(str(file_URL))

