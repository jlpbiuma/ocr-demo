import pytesseract
from functions.readImage import extract_text_from_pdf

# Tell pytesseract where your Tesseract OCR is
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Your PDF file path
pdf_file = './data/Test.pdf'
# Folder to save extracted images
image_folder = './images'
# Poppler path
poppler_path = r'C:\\poppler_v2\\Library\bin'

extract_text_from_pdf(pdf_file, image_folder, poppler_path)