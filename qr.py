import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "any website link that you want to add"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scale = 8) 