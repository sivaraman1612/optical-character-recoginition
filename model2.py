import cv2
import pytesseract
image = cv2.imread('img.png')

if image is None:
    print("Error: input.jpg not found!")
    exit()

image = cv2.resize(
    image,
    None,
    fx=2,
    fy=2,
    interpolation=cv2.INTER_CUBIC
)
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)
gray = cv2.GaussianBlur(
    gray,
    (5, 5),
    0
)
_, threshold = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
cv2.imwrite(
    "processed.jpg",
    threshold
)
config = "--psm 6"
text = pytesseract.image_to_string(
    threshold,
    config=config
)

print("     EXTRACTED TEXT")


print(text)


with open(
    "output.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(text)

