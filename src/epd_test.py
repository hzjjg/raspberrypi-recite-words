# 测试电子墨水屏的显示

import logging

from PIL import Image
from draw import draw
from dict import query
from dep.epd import epd as Epd

img = draw(query('good'))
img = img.transpose(Image.ROTATE_180)

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
