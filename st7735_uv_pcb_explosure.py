import sys

from PIL import Image
import ST7735 as ST7735

print("""
image.py - Display an image on the LCD.

If you're using Breakout Garden, plug the 0.96" LCD (SPI)
breakout into the rear slot.
""")

if len(sys.argv) < 2:
    print("Usage: {} <image_file>".format(sys.argv[0]))
    sys.exit(1)

image_file = sys.argv[1]

# Create ST7735 LCD display class.
disp = ST7735.ST7735(
    port=0,
    cs=0,  # BG_SPI_CSB_BACK or BG_SPI_CS_FRONT
    dc=24,
    backlight=None,
    rst=25, 
    width=128, 
    height=160, 
    rotation=90, 
    invert=False,               # 18 for back BG slot, 19 for front BG slot.
    spi_speed_hz=4000000
)

WIDTH = disp.width
HEIGHT = disp.height

# Initialize display.
disp.begin()

# Load an image.
print('Loading image: {}...'.format(image_file))
image = Image.open(image_file)

# Resize the image
image = image.resize((WIDTH, HEIGHT))

# Draw the image on the display hardware.
print('Drawing image')

disp.display(image)


