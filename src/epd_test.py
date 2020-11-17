import logging
from draw import draw
from dep.epd import epd as Epd

img = draw({
    'word': 'good'
})

try:
    logging.info("Demo")

    epd = Epd.EPD()
    logging.info("init and Clear")
    epd.init(epd.lut_full_update)
    epd.Clear(0xFF)

    epd.display(epd.getbuffer(img))
except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    Epd.epdconfig.module_exit()
    exit()