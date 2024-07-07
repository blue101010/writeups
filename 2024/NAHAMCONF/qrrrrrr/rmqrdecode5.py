# Script 1: Display the binary image and plot sum along width and height

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the image
image_path = 'qrrrrrrrr.png'  # Update the path if needed
img = Image.open(image_path)

# Convert image to grayscale
img_gray = img.convert('L')
# Convert to numpy array
img_array = np.array(img_gray)
# Apply a threshold to get a binary image (0 or 255)
binary_image = (img_array < 128).astype(np.uint8)

# Sum along the width and height to find the number of unique columns and rows
sum_width = np.sum(binary_image, axis=0)
sum_height = np.sum(binary_image, axis=1)

# Display the image to visually inspect the modules
plt.xticks(np.arange(0, len(sum_width), 20), rotation='vertical')  # Adjusting sub-graduations to every 20 steps with vertical text
plt.yticks(np.arange(0, 151, 10))  # Y-axis with 10px subunits, up to 150  
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.imshow(binary_image, cmap='gray')
plt.show()
# # Plot the sum arrays to visualize the transitions
# plt.figure(figsize=(12, 6))
# plt.suptitle("Analysis of QR Code Structure")  # Overall title for the figure

# plt.subplot(1, 2, 1)
# plt.plot(sum_width, label="Sum Width")
# plt.title("Sum along width")
# plt.xlabel("Width")
# plt.ylabel("Sum")
# plt.xticks(np.arange(0, len(sum_width), 10))  # Adding sub-graduations every 10 steps
# plt.yticks(np.arange(0, max(sum_width)+1, 10))  # Y-axis with 10px subunits
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.legend()  # Adding a legend

# plt.subplot(1, 2, 2)
# plt.plot(sum_height)
# plt.title("Sum along height")
# plt.xlabel("Height")
# plt.ylabel("Sum")
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for the overall title
# plt.show()