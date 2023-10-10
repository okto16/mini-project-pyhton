import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Okto Datte\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
img = Image.open('sri1.jpeg')
text = tess.image_to_string(img)
print(text)