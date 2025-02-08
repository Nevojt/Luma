# python -m pip install segno
# https://realpython.com/python-generate-qr-code/

# import segno
#
# qrcode = segno.make_qr("Hello, World")
# qrcode.save("basic_qrcode.png", scale=5, light="lightblue",dark="darkblue",quiet_zone="maroon", data_dark="green")

# python -m pip install pillow qrcode-artistic

import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
nirvana_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
slts_qrcode.to_artistic(
    background=nirvana_url,
    target="animated_qrcode.gif",
    scale=5,
)
