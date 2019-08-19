import RPi.GPIO as IO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#Setup Display
RST = 24
disp = None

def setup_display(address):
    disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_address=address)
    disp.begin()
    return disp

try:
    disp = setup_display(0x3C)
except OSError:
    disp = setup_display(0x3D)

#Clear Display
disp.clear()
disp.display()

#Create blank image for drawing with 1 for 1 bit color
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

#Make draw object draw on image
draw = ImageDraw.Draw(image)

#Clear the image
draw.rectangle((0, 0, width, height), outline = 0, fill = 0)

#Load default font
font = ImageFont.load_default()

while True:
    IO.setmode(IO.BCM)
    IO.setup(21, IO.IN)
    if IO.input(21):
        draw.text((6, 0), "INFRARED SENSOR:", font=font, fill=455)
        draw.text((16, 12),   'MOTION DETECTED',   font=font, fill=455)
    else:
        draw.text((6, 0), "INFRARED SENSOR:", font=font, fill=455)
        draw.text((10, 12),   'NO MOTION DETECTED',   font=font, fill=455)
    disp.image(image)
    disp.display()
    time.sleep(1)
    disp.clear()
    draw.rectangle((0, 0, width, height), outline = 0, fill = 0)
    IO.cleanup()
    time.sleep(1)
