"""
Reference:
https://www.geeksforgeeks.org/python-pil-image-split-method/#:~:text=image%20editing%20capabilities.-,Image.,red%2C%20green%2C%20blue).
"""

from PIL import Image

# opening a multiband image (RGB specifically)
image = Image.open(r"images/ImagenUsar.jpg")

# split() method
# this will split the image in individual bands and return a tuple
image = Image.Image.split(image)

# showing each band
red = image[0]
green = image[1]
blue = image[2]

red.save("images/red.jpg")
green.save("images/green.jp")
blue.save("images/blue.jpg")
