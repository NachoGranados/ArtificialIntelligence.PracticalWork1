# libraries
from PIL import Image
import numpy as np
from constants import *

"""
This function returns the array of the
received image

Input:
image -> image for array generation

Outputs:
imageArray -> image array
"""
def getImageArray(image):

    # generate array from image
    imageArray = np.asarray(image)

    return imageArray

"""
This function returns the image of the
received array

Input:
imageArray -> image array

Outputs:
image -> generated image
"""
def getImage(imageArray):

    # generate image from array
    image = Image.fromarray(imageArray)

    return image

"""
This function returns the dimensions of the
received image array

Input:
imageArray -> image array

Outputs:
rows -> number of rows
columns -> number of columns
colors -> number of colors
"""
def getShape(imageArray):

    # get image array dimensions
    rows = imageArray.shape[0]
    columns = imageArray.shape[1]
    colors = imageArray.shape[2]

    return rows, columns, colors

"""
This function reshapes a 2D array into 3D array
and saves it

Input:
imageArray -> image array

Output:
reshapedImageArray -> reshaped image array
"""
def reshape3Dto2D(imageArray):

    # get dimensions
    rows, columns, colors = getShape(imageArray)

    # reshape 3D image array into 2D image array
    reshapedImageArray = np.reshape(imageArray,(rows, columns * colors))
    
    # generate image from array
    reshapedImage = Image.fromarray(reshapedImageArray)

    # save generated image
    reshapedImage.save(STORAGE_DIRECTORY_REMODELING + "reshaped2D.jpg")

    return reshapedImageArray

"""
This function reshapes a 2D array into 3D array
and saves it

Inputs:
orginalImageArray -> orginal image array
reshapedImageArray -> reshaped image array

Output:
reshapedReshapedImage -> reshaped image array
"""
def reshape2Dto3D(orginalImageArray, reshapedImageArray):

    # get array from orginalImage
    #orginalImageArray = getImageArray(orginalImageArray)

    # get dimensions of orginalImage
    rows, columns, colors = getShape(orginalImageArray)

    # get array from reshapedImageArray
    #reshapedImageArray = np.asarray(reshapedImageArray)

    # reshape 2D image array into 3D image array
    reshapedReshapedImageArray = np.reshape(reshapedImageArray,(rows, columns, colors))

    # generate image from array
    reshapedReshapedImage = Image.fromarray(reshapedReshapedImageArray)

    # save generated image
    reshapedReshapedImage.save(STORAGE_DIRECTORY_REMODELING + "reshaped3D.jpg")

    return reshapedReshapedImage

"""
This function splits the received image into
RGB bands and saves them

Input:
image -> image to split

Outputs:
red -> red scale image
green -> green scale image
blue -> blue scale image
"""
def splitImage(image):    

    # split image in individual RGB bands
    splittedImage = Image.Image.split(image)

    # assign RGB band images
    red = splittedImage[0]
    green = splittedImage[1]
    blue = splittedImage[2]

    # save RGB band images
    red.save(STORAGE_DIRECTORY_LAYER + "red.jpg")
    green.save(STORAGE_DIRECTORY_LAYER + "green.jpg")
    blue.save(STORAGE_DIRECTORY_LAYER + "blue.jpg")

    return red, green, blue

"""
This function merges the received images into
single RGB image and saves it

Inputs:
red -> red scale image
green -> green scale image
blue -> blue scale image

Output:
merge -> merged image
"""
def mergeImages(red, green, blue):    

    # convert RGB band images to grayscale
    red = red.convert("L")
    green = green.convert("L")
    blue = blue.convert("L")

    # merge RGB band images
    merge = Image.merge("RGB", (red, green, blue))

    # save merged RGB band images
    merge.save(STORAGE_DIRECTORY_LAYER + "merge.jpg")

    return merge
