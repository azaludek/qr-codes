# Import libraries
import qrcode # Generate QR codes
from PIL import Image # This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities

# Set value to variable "data"
data = 'https://azaludek.github.io'

# Styling the QR code
qr = qrcode.QRCode(version = 1, box_size=10, border=5)

# Add "data" to QR code and create the QR code itself
qr.add_data(data)

# Additional styling
qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

# Saving the created QR code
img.save('qr-code/qr-to-web-customized.png') # Set where you want to store final image of the QR code and name it
