import segno
from urllib.request import urlopen


qrcode = segno.make_qr("https://realpython.com/python-generate-qr-code/")
url_open = urlopen("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWRxMGJuaG1zYTg2YzR6ejY4ZnMwdjVvOXQ3ZDNwdnViaGpvZTM1aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GdRG4WHGgmNTq/giphy.gif")
qrcode.to_artistic(
    background=url_open,
    target="animated-qr.gif",
    scale=5
)


# qrcode.save("qr-test.png")