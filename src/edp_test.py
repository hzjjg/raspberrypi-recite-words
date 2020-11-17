import logging
from draw import draw
import lib.edp.edp as Edp

img = draw({
    'word': 'good'
})

try:
    logging.info("Demo")

    epd = Edp.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    epd.display(epd.getbuffer(img))
except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    Edp.epdconfig.module_exit()
    exit()
