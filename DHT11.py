import sys
import Adafruit_DHT
import time
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

# First define some constants to allow easy resizing of shapes.
padding = 2
top = padding
bottom = height-padding

while True:
    #Display humidity and temperature
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((padding, -2),    'DHT11 Sensor',  font=font, fill=455)
    draw.text((padding, 8),   'Temperature: ' +  str(temperature) + "C",   font=font, fill=455)
    draw.text((padding, 18),    'Humidity: ' + str(humidity) + "%" ,  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    #time.sleep(1)
