import qrcode
data="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"
qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='black',back_color='white')
img.save('gmail.png')
