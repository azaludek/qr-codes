from pyzbar.pyzbar import decode 
from PIL import Image

img = Image.open('QR CODE IMAGE LOCATION')

result = decode(img)

print(result)