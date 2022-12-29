#šifrování QR kódu
import qrcode
from PIL import Image


data = 'https://azaludek.github.io'

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('qr-code/qr-to-web-customized.png') #Set where you want to store final image of the QR code and name it
