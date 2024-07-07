import cv2
import numpy as np
import os

import math

import cv2

def estimate_rmqr_module_size(image_path):
    """
    Estimate the number of vertical and horizontal modules in an rMQR code image.
    
    Args:
        image_path (str): The path to the rMQR code image file.
        
    Returns:
        tuple: A tuple containing the number of vertical and horizontal modules, or None if the image is not a valid rMQR code.

    The estimation is that the QR has 11 vertical modules and 59 horizontal modules. So an R11X59 RMQR code.
    Based on documentation https://www.qrcode.com/en/codes/rmqr.html
    An R11 RMQR can have 6 types patterns of horizontal modules (27, 43,59,99 or 139 modules)
   27 modules is one pattern, 43 modules 2 patterns, 59 modules is 3 patterns...etc
    """
    # Define the available rMQR code sizes
    sizes = [(7, 43), (9, 43), (11, 43), (13, 43), (15, 43), (17, 43),
             (7, 59), (9, 59), (11, 59), (13, 59), (15, 59), (17, 59),
             (7, 77), (9, 77), (11, 77), (13, 77), (15, 77), (17, 77),
             (7, 99), (9, 99), (11, 99), (13, 99), (15, 99), (17, 99),
             (11, 139), (13, 139), (15, 139), (17, 139)]
    
    # Load the image
    img = cv2.imread(image_path)
    
    # Get the image dimensions
    height, width = img.shape[:2]
    
    # Iterate over the available rMQR code sizes
    for rows, cols in sizes:
        # Calculate the module size for the current rMQR code size
        module_size_x = width / cols
        module_size_y = height / rows
        
        # Check if the module sizes are approximately equal
        if abs(module_size_x - module_size_y) < 1:
            return rows, cols
    
    # If no suitable size is found, return None
    return None


def is_valid_rmqr_code(image_path):
    """
    Checks if the image is a valid rMQR code and displays all the properties and test results.

    Args:
        image_path (str): The path to the image file.

    Returns:
        bool: True if the image is a valid rMQR code, False otherwise.
    """
    # Load the image
    img = cv2.imread(image_path)

    # Get the image dimensions
    height, width, _ = img.shape

    # Calculate the aspect ratio
    aspect_ratio = width / height

    # Print the image default properties
    print(f"Image Size: {width} x {height} pixels")
    print(f"Aspect Ratio: {aspect_ratio:.2f}")

    # Estimate the number of vertical and horizontal modules
    rows, cols = estimate_rmqr_module_size(image_path)
    if rows and cols:
        print(f"The estimation is that the QR has {rows} vertical modules and {cols} horizontal modules. So an R{rows}X{cols} RMQR code.")
 

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to binarize the image
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Find contours in the binarized image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours to find the rMQR code
    rmqr_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Adjust this threshold as needed
            rmqr_contour = contour
            break

    if rmqr_contour is not None:
        # Extract the rMQR code region from the image
        x, y, w, h = cv2.boundingRect(rmqr_contour)
        rmqr_roi = img[y:y+h, x:x+w]

        # Check if the extracted region is an rMQR code
        is_valid = validate_rmqr_code(rmqr_roi)

        # if is_valid:
        #     print("\nOverall hypothesis: The image is a valid rMQR code.")
        #     return True
        # else:
        #     print("\nOverall hypothesis: The image is unlikely to be an rMQR code.")
        #     return False
    else:
        print("No rMQR code found in the image.")
        return False

def validate_rmqr_code(rmqr_roi):
    """
    Validates the rMQR code region and displays the test results.

    Args:
        rmqr_roi (numpy.ndarray): The image region containing the rMQR code.

    Returns:
        bool: True if the region is a valid rMQR code, False otherwise.
    """
    # Check if the image region has the expected aspect ratio
    height, width = rmqr_roi.shape[:2]
    aspect_ratio = width / height
    if aspect_ratio < 0.5 or aspect_ratio > 8.2:
        print("Aspect ratio test failed: Aspect ratio is {:.2f}, which is outside the expected range.".format(aspect_ratio))
        return False

    # Check for the presence of the position detection patterns
    gray = cv2.cvtColor(rmqr_roi, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the binarized image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Check for the presence of three position detection patterns
    position_patterns = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # Adjust this threshold as needed
            position_patterns.append(contour)

    # if len(position_patterns) != 3:
    #     print("Position detection patterns test failed: Found {} position detection patterns, expected 3.".format(len(position_patterns)))
    #     return False
    # else:
    #     print("Position detection patterns test passed: Found 3 position detection patterns.")

    # Check the position and arrangement of the position detection patterns
    # Implement your logic here based on the rMQR code specification
    # ...

    print("All tests passed: The image region is a valid rMQR code.")
    return True

def decode_rmqr_code(image_path):
    """
    Decodes the rMQR code from the given image file.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The decoded data if the image is a valid rMQR code, None otherwise.
    """
    if is_valid_rmqr_code(image_path):
        # Load the image
        img = cv2.imread(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply adaptive thresholding to binarize the image
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        # Find contours in the binarized image
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Filter contours to find the rMQR code
        rmqr_contour = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 1000:  # Adjust this threshold as needed
                rmqr_contour = contour
                break

        if rmqr_contour is not None:
            # Extract the rMQR code region from the image
            x, y, w, h = cv2.boundingRect(rmqr_contour)
            rmqr_roi = img[y:y+h, x:x+w]

            # Implement your logic here to decode the rMQR code
            decoded_data = decode_rmqr_code_region(rmqr_roi)
            return decoded_data
        else:
            print("No rMQR code found in the image.")
            return None
    else:
        return None

# Helper function to decode the rMQR code region
# You'll need to implement this based on the rMQR code specification
def decode_rmqr_code_region(rmqr_roi):
    # Implement your rMQR code decoding logic here
    # ...
    return "Decoded data"

# Example usage
image_path = "qrrrrrrrr.png"  # Replace with your actual image filename or path
decoded_data = decode_rmqr_code(image_path)
if decoded_data:
    print(f"Decoded rMQR code: {decoded_data}")
