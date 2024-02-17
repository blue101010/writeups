#!/usr/bin/python
#https://security.stackexchange.com/questions/151196/steganography-jpegsnoop

from PIL import Image

def main():
  """
  This function opens an image file named "output.jpg", converts it to the YCbCr color space,
  splits the image into its Y, Cb, and Cr channels, and prints any pixel values in the Y channel
  that are greater than 255. If any modifications are made, it saves the modified image as "output1.jpg".
  """
  print("Opening the image file...")
  im = Image.open("output.jpg")
  print("Image file opened successfully.")

  print("Converting the image to the YCbCr color space...")
  im = im.convert("YCbCr")
  print("Image converted successfully.")

  print("Splitting the image into its Y, Cb, and Cr channels...")
  y, cb, cr = im.split()
  print("Image split successfully.")

  print("Getting the pixel values from the Y channel...")
  seq = list(y.getdata())
  print("Pixel values obtained successfully.")

  modified = False

  print("Checking for pixel values greater than 255...")
  for i, x in enumerate(seq):
    if x > 255:
      print("Found a pixel value greater than 255:", x)
      seq[i] = 255
      modified = True

  if modified:
    print("Modifying the image...")
    y.putdata(seq)
    im = Image.merge("YCbCr", (y, cb, cr))
    im.save("output1.jpg")
    print("Image modified successfully. Saved as output1.jpg.")
  else:
    print("No modification.")

if __name__ == '__main__':
  main()