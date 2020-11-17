import logging
from draw import draw
from dep.epd.epd import Epd

img = draw({
    'word': 'good'
})

try:
    logging.info("Demo")

    epd = Epd.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    epd.display(epd.getbuffer(img))
except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    Epd.epdconfig.module_exit()
    exit()
