"""
Reference:
https://gis.stackexchange.com/questions/180534/merge-rgb-band-using-python
"""

from PIL import Image

red = Image.open("images/red.jpg").convert("L")
green = Image.open("images/green.jpg").convert("L")
blue = Image.open("images/blue.jpg").convert("L")

merge = Image.merge("RGB", (red, green, blue))
merge.save("images/merge.jpg")
