import qrcode

url = input("Enter URL here: ")
filename = input("Enter filename to save the QR code: ")

img = qrcode.make(url)
img.save(filename + ".png")

print("QR code is generated Successfully")
print("Thank You!")
