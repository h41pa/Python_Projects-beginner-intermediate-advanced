import qrcode


def generate_QrCode(text):
    qr = qrcode.main.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('qrimg001.png')


url = input("Enter your url: ")
generate_QrCode(url)
