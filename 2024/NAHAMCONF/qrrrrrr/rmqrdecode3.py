from PIL import Image

# Load the image
image_path = 'qrrrrrrrr.png'
img = Image.open(image_path)

# Get image dimensions
width, height = img.size

# Display the width and height
print("Image width:", width)
print("Image height:", height)
