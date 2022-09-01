from functions import *
from constants import *

"""
This method flattens the third dimension of the image array into
the second dimension using the reshape method, applies PCA, and
rebuilds as a three-dimensional array.
"""
def remodelingMethod():

    # open original image
    originalImage = Image.open(STORAGE_DIRECTORY + ORIGINAL_IMAGE)

    # show original image
    originalImage.show()

    # get image array
    originalImageArray = getImageArray(originalImage)

    # reshape image array from 3D to 2D
    reshapedImageArray = reshape3Dto2D(originalImageArray)

    # calculate PCA
    # reshapedPCA = PCA(reshapedImageArray)

    """
    for k in K_ARRAY:
        imageArray = PCA(k)
        image = getImage(imageArray)
        image.save(k + "merge.jpg")
    """

    # reshape image array from 2D to 3D
    reshapedImageArray = reshape2Dto3D(originalImageArray, reshapedImageArray)  

"""
This method treats a color image as a stack of 3 separate 2D images
(red, blue, and green layers). The truncated PCA reconstruction is
applied to each two-dimensional layer separately, and then the
reconstructed layers are rejoined.
"""
def layerMethod():
    
    # open original image
    originalImage = Image.open(STORAGE_DIRECTORY + ORIGINAL_IMAGE)

    # show original image
    originalImage.show()

    # split image in RGB bands
    red, green, blue = splitImage(originalImage)

    # get red image array
    redImageArray = getImageArray(red)

    # get green image array
    greenImageArray = getImageArray(green)

    # get blue image array
    blueImageArray = getImageArray(blue)

    # calculate red layer PCA
    #redPCA = PCA(redImageArray)

    # calculate green layer PCA
    #greenPCA = PCA(greenImageArray)

    # calculate blue layer PCA
    #bluePCA = PCA(blueImageArray)

    """
    for k in K_ARRAY:
        imageArray = PCA(k)
        image = getImage(imageArray)
        image.save(k + "merge.jpg")
    """

    # merge RGB bands
    merge = mergeImages(red, green, blue)

remodelingMethod()
layerMethod()
