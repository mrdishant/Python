from PIL import Image
import pytesseract



text=pytesseract.image_to_string(Image.open('test.jpeg'))
# text=pytesseract.image_to_string(Image.open('test.jpeg'), lang='eng')
print (text)

f = open("parkingsites.txt","w+")

f.write(text)

