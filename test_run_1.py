from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'd:\\Tesseract\\tesseract.exe'

text = pytesseract.image_to_string(Image.open('.\\test_images\\trukk_stats.png'))
print(text)