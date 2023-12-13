import pytesseract
from functions.readImage import extract_text_from_pdf

# Tell pytesseract where your Tesseract OCR is
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Assuming it's in the default location within the container

# Your PDF file path within the container
pdf_file = '/app/data/Test.pdf'  # Adjust the path based on your container's file structure

# Folder to save extracted images within the container
image_folder = '/app/images'  # Adjust the path based on your container's file structure

# Poppler path within the container
poppler_path = '/usr/bin'  # Adjust the path based on your container's file structure

text = extract_text_from_pdf(pdf_file, image_folder, poppler_path)

# Print the extracted text
print(text)