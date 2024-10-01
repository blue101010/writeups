import cv2
import numpy as np
from pyzbar.pyzbar import decode
from matplotlib import pyplot as plt

# Load the image
image_path = 'PixelErr.png'
img = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to convert the grayscale image into binary
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Optionally, show the binary image
plt.imshow(binary, cmap='gray')
plt.title("Binary Image")
plt.show()

# Decode the QR code from the binary image
decoded_objects = decode(binary)

# Loop over all decoded objects
for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode('utf-8'))

if not decoded_objects:
    print("No QR code detected.")
