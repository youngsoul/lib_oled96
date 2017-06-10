#!/usr/bin/env python

from lib_oled96 import ssd1306
from PIL import Image, ImageDraw, ImageFont
import time


oled = ssd1306(flip_screen=True)   # create oled object, nominating the correct I2C bus, default address
while True:
        # we are ready to do some output ...
        fnt = ImageFont.truetype('/home/pi/oled/lib_oled96/FreeMono.ttf', 18)
        fnt2 = ImageFont.truetype('/home/pi/oled/lib_oled96/FreeMono.ttf', 24)

        # put border around the screen:
        oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)

        # Write two lines of text.
        oled.canvas.text((4,4), 'Temperature', font=fnt, fill=1)
        oled.canvas.text((40,30),    '72.4 F', font=fnt2,  fill=1)

        # now display that canvas out to the hardware
        oled.display()

        time.sleep(3)

        oled.cls()

        # put border around the screen:
        oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)


        # Write two lines of text.
        oled.canvas.text((4,4), 'Moisture', font=fnt, fill=1)
        oled.canvas.text((40,30),    '18.3 %', font=fnt2,  fill=1)

        oled.display()

        time.sleep(3)
        oled.cls()

