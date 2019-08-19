import RPi.GPIO as IO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import board
from digitalio import DigitalInOut, Direction

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
    pad_pin = board.D11
    pad = DigitalInOut(pad_pin)
    pad.direction = Direction.INPUT
    if pad.value:
        draw.text((6, 0), "Digital Touch Sensor", font=font, fill=455)
        draw.text((40, 15),   'PRESSED',   font=font, fill=455)
    else:
        draw.text((6, 0), "Digital Touch Sensor", font=font, fill=455)

    disp.image(image)
    disp.display()
    time.sleep(0.1)
    disp.clear()
    draw.rectangle((0, 0, width, height), outline = 0, fill = 0)
    IO.cleanup()
    time.sleep(0.1)
