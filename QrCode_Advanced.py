import qrcode as q
from PIL import Image

qr = q.QRCode(version=1, error_correction=q.constants.ERROR_CORRECT_H, box_size=10, border=4)

qr.add_data("www.amazon.in")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="pink")
img.save("Amazon Webpage.png")
