# Child Safety AI QR

Child Safety AI QR is a web application designed to enhance child safety by converting filled forms into AI art QR codes. These QR codes can be printed as stickers, keychains, badges, and more. In the event of an emergency or when a child is lost, anyone with a QR scanner can access the child's details in a PDF format. This project was developed in Python and deployed on Streamlit. You can access the live demo [here](https://childsafetyaiqr.streamlit.app/).

## Features

- Fill out a child's details and generate an AI art QR code containing a link to the PDF form.
- Download the PDF form or print the QR code for physical use.
- Leveraging Filestack for PDF storage and the Hugging Face API for the model (ControlNet_QRCode-Control_v1p_sd15) through Gradio.

## Project Demo

Check out a video demonstration of our project on YouTube:

[![Project Demo Video](https://img.youtube.com/vi/q7eXclpiRsc/0.jpg)](https://www.youtube.com/watch?v=q7eXclpiRsc)

In this video, you'll see how to use the Child Safety AI QR web application and get a closer look at its features.

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ChildSafetyAIQR.git
   cd ChildSafetyAIQR
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open your web browser and go to `http://localhost:8501` to use the application.

## Usage

1. Fill out the child's details in the form.
2. Click the "Generate QR Code" button to create an AI art QR code.
3. Download the PDF form or print the QR code as needed.

## Collaborators

- [Souradip Pal](https://github.com/SparklinStar)
- [Baivab Mukhopadhyay](https://github.com/itsBaivab)
- [Disha Karmakar](https://github.com/dishakarmakar1210)
- [Aishi Chakraborty](https://github.com/aishi07)

## Acknowledgments

- Special thanks to the [Hugging Face](https://huggingface.co/) community for their AI model.
- [Filestack](https://www.filestack.com/) for PDF storage.
- [Gradio](https://www.gradio.app/) for integrating the Hugging Face model.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
