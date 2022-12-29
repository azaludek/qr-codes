# Import libraries
from pyzbar.pyzbar import decode # Read one-dimensional barcodes and QR codes from Python 2 and 3 using the zbar library
from PIL import Image # Image module, also provides a number of factory functions, including functions to load images from files, and to create new images

# Find the QR code you want to decode in files
img = Image.open('QR CODE IMAGE LOCATION')

# Decode the image stored in img variable
result = decode(img)

# Print out the result
print(result)
