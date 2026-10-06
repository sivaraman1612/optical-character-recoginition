#this use easyocr model for optical character recognition
import easyocr

reader = easyocr.Reader(['en'])

result = reader.readtext('/home/sivaraman/Documents/kiwistron/ocr/input.jpg')

for detection in result:
    print(detection[1])