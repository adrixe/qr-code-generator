import qrcode
from random import randint

data = input("Enter text/URL to convert into a QR Code: ")
filename = f"qrcode_{randint(1000,9999)}.png"
qrcode.make(data).save(filename)
print(f"QR Code saved as {filename}")
