from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import cv2
import pytesseract
import os

def extract_text_from_pdf(pdf_file, image_folder, poppler_path):
    # Extract images from PDF and get their paths
    image_paths = list(extract_images_from_pdf(pdf_file, image_folder, poppler_path))
    # Process each image with Tesseract OCR
    text = ''
    for image_path in image_paths:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        text += pytesseract.image_to_string(threshold_img)
    # Save to text file
    with open('extracted_text.txt', 'w') as f:
        f.write(text)
    # Delete all the images
    for image_path in image_paths:
        os.remove(image_path)
    return text
        
# Function to extract images from a PDF
def extract_images_from_pdf(pdf_path, image_folder, poppler_path):
    pdf_reader = PdfReader(pdf_path)
    # Iterate through all pages
    for page_num in range(len(pdf_reader.pages)):
        # Convert each page to an image
        images = convert_from_path(pdf_path, first_page=page_num + 1, last_page=page_num + 1, poppler_path=poppler_path)
        for i, image in enumerate(images):
            # Save each image to the specified folder
            image_path = f"{image_folder}/page_{page_num + 1}_img_{i + 1}.png"
            image.save(image_path, 'PNG')
            yield image_path