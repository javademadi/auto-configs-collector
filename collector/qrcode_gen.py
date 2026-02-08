import qrcode

def make_qr(text, path):
    img = qrcode.make(text)
    img.save(path)
