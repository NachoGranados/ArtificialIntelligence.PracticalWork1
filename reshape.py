"""
Example for 3D array
[[[ 5  4 ] [ 6  9 ]]

 [[ 1  0 ] [ 9  5 ]]

 [[ 4  9 ] [13 19 ]]

 [[ 8 10 ] [ 1  5 ]]]

Shape: (4, 2, 2)

--------------------

Example for 2D array
[[ 5  4  6  9 ]
 [ 1  0  9  5 ]
 [ 4  9 13 19 ]
 [ 8 10  1  5 ]]

Shape: (4, 4)

"""

"""
Reference:
https://www.pythonpool.com/numpy-reshape-3d-to-2d/
"""

from PIL import Image
import numpy as np

# open image
image = Image.open('images/ImagenUsar.jpg')

# generate array from image
imageArray = np.asarray(image)

# get image array dimensions
rows = imageArray.shape[0]
columns = imageArray.shape[1]
colors = imageArray.shape[2]

print(" ")
print(imageArray)
print(" ")
print(rows, columns, colors)
print(" ")

# reshape 3D image array into 2D image array
reshapedImageArray = np.reshape(imageArray,(rows, columns * colors))
print(reshapedImageArray)
print(" ")

# generate image from array and save it
reshapedImage = Image.fromarray(reshapedImageArray)
reshapedImage.save('images/reshaped.jpg')

# reshape 2D image array into 3D image array
reshapedReshapedImageArray = np.reshape(reshapedImage,(rows, columns, colors))
print(reshapedReshapedImageArray)
print(" ")

# generate image from array and save it
reshapedReshapedImage = Image.fromarray(reshapedReshapedImageArray)
reshapedReshapedImage.save('images/reshapedReshaped.jpg')
