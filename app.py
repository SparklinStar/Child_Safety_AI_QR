import streamlit as st
import QR_Gen
import pdf_create as pdf
from PIL import Image
import style

page_bg_img = style.stylespy()  # used for styling the page

# Appname
st.set_page_config(page_title="Child Safety QRAI 🖌️", layout="wide")

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #fff;'>Child Safety QR.AI 🖌️</h1>", unsafe_allow_html=True)

# Split the page into two columns
col1, col2 = st.columns(2, gap='medium')

# Form UI in the first column
with st.form(key="form1"):
    with col1:
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        Name = st.text_input('Enter First name')
        Address = st.text_input('Enter your address')
        Birthday = st.date_input('Your birthday')
        Gender = st.radio('Gender', ['Male', 'Female', 'Others'])
        Contact = st.text_input('Enter your contact number')
        anothercontact = st.text_input('Enter another contact number')
        Contact_Email = st.text_input('Enter Contact email address')
        FathersName = st.text_input("Enter Father's name")

    with col2:
        MothersName = st.text_input('Enter Mother"s name')
        SchoolName = st.text_input('Enter your school name')
        SchoolAddress = st.text_input('Enter your school address')
        city = st.text_input('City')
        state = st.text_input('State')
        ZipCode = st.text_input('Zip code')
        Country = st.text_input('Country')
        Blood_Group = st.selectbox('Blood Group', ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
        Identification_mark = st.text_input('Identification mark')
        Allergenes = st.text_input('Allergenes')

# Controlnet UI in the second column
    with col2:
        st.title("AI Configuration")

        input_choice = st.radio("Select Input Type", ["Dropdown", "Text Field"])
        p_prompt = ""

        if input_choice == "Dropdown":
            dropdown_choice = st.selectbox("Select promopt", [
                "Sky view of highly aesthetic, ancient greek thermal baths in beautiful nature",
                "Bright sunshine coming through the cracks of a wet, cave wall of big rocks",
                "A sky view of colorful lakes and rivers flowing through the desert",
                "Concept art: A surreal sight of a crystal-clear lake in the middle of the desert, reflecting the stars of the Milky Way. The juxtaposition of the arid landscape and the tranquil waters adds a dream-like quality to the scene",
                "Sunlight filtering through a dense forest, creating a magical glow",
                "In the heart of the tranquil woods, nature's embrace reveals a realm of enchanting radiance",
                "Blended"
            ])
            p_prompt = dropdown_choice
            st.write("Selected:", dropdown_choice)
        else:
            text_input = st.text_input("Enter your prompt here")
            p_prompt = text_input
            st.write("Entered:", text_input)

        
        seed = st.slider('Seed value', -1, 9999999999, 9635874126)
    genarate = st.form_submit_button(label="Generate", use_container_width=True)
