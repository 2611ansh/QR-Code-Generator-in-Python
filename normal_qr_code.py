# import module
import qrcode as qr

# make function is used to create a QR code
# save is used to save the QR code in png format

img = qr.make("https://github.com/2611ansh?tab=repositories")
img.save("github_qr.png")