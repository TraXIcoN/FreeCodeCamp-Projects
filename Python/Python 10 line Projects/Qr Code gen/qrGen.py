import pyqrcode
import qrcode
def qrCode(data):
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("result.jpg")

info = f'''
    Email : "test@check.com"
    '''
qrCode(info)
