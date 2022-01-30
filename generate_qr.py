import qrcode
import cv2
from pyzbar.pyzbar import decode
from PIL import Image

def new_qr(id_msg, url, ver=1, b_size=10, brd=4, bg_color="white", f_color="black"):
    qr = qrcode.QRCode(
        version=ver,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=b_size,
        border=brd,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=f_color, back_color=bg_color)

    qr_name = 'qrcods/' + str(id_msg) + '.png'
    img.save(qr_name)


def decoder_qr(id_msg):
    filename = 'qrcods/' + str(id_msg) + '.png'

    img = Image.open(filename)
    decoded = decode(img)
    return decoded[0].data.decode("utf-8")
    # img = cv2.imread(filename)
    # # data, bbox, clear_qrcode = cv2.QRCodeDetector().detectAndDecode(img)
    # # print(data)
    # # print(bbox)
    # # cv2.imshow('rez', clear_qrcode)
    # # cv2.waitKey(0)
    # # return data
