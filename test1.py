#!/usr/bin/env python

from lib_oled96 import ssd1306
from PIL import Image, ImageDraw, ImageFont

oled = ssd1306(flip_screen=True)   # create oled object, nominating the correct I2C bus, default address

# we are ready to do some output ...
fnt = ImageFont.truetype('/home/pi/oled/lib_oled96/FreeMono.ttf', 18)

# put border around the screen:
oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)

# Write two lines of text.
oled.canvas.text((4,4), 'HelloWWWWW', font=fnt, fill=1)
oled.canvas.text((40,40),    'World!', font=fnt,  fill=1)

# now display that canvas out to the hardware
oled.display()
