import pyqrcode
import png
from pyqrcode import QRCode

# data inside the qrcode
data = "Hello, World"

# filename of the given png or svg
filename = "[YOUR-FILENAME]"

# size of the qr code
scale=8

# NO USER CHANGEABLE VARIABLES BEYOND THIS COMMENT

# generate qr code
code = pyqrcode.create(data)

# generate qr code's svg
code.svg("qrcodes/" + filename + ".svg", scale=scale)

# generate qr code's png
code.png("qrcodes/" + filename + ".png", scale=scale)