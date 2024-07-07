from PIL import Image
import numpy as np

# Load an image
img = Image.open('qrrrrrrrr.png')  # Update the path to your image file

# Convert image to grayscale
img_gray = img.convert('L')
# Convert to numpy array
img_array = np.array(img_gray)
# Apply a threshold to get a binary image (0 or 255)
binary_image = (img_array < 128).astype(np.uint8)

# Sum along the width and height to find the number of unique columns and rows
sum_width = np.sum(binary_image, axis=0)
sum_height = np.sum(binary_image, axis=1)

# Count changes from 0 to 1 or 1 to 0 to determine the number of modules
width_modules = np.count_nonzero(np.diff(sum_width))
height_modules = np.count_nonzero(np.diff(sum_height))

print("Number of modules in width:", width_modules)
print("Number of modules in height:", height_modules)