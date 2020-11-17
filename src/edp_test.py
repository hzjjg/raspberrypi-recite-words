import lib.edp.edp as edp
from draw import draw
import time
stimport logging

img = draw({
    'word': 'good'
})

try:
    logging.info("Demo")

    epd = edp.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    epd.display(epd.getbuffer(img))
