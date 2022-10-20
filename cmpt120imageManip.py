# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Saurab Dhir
# Date: 19th November, 2020
# Description: File where all the image manipulation/handling takes place
# Copyleft, all wrongs reserved

# Basic Functions:

# Scan Row in image
# Scan Pixel in image
# Set RGB values in image as the opposite of themselves
# IE: R = 255-R
def invertImage(image):
    # code
    for pixelRow in image:
        for pixel in pixelRow:
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
    return image


# Scan image to half the height (so as to not copy the manipulations back lmao)
# Get Height, Width, and then replace scanned pixel with opposite end pixel
# For example:
#    a b c               a b c
#   #######             #######
# a #1 2 3#           a #3 2 1#
# b #4 5 6#      =    b #6 5 4#
# c #7 8 9#           c #9 8 7#
#   #######             #######
#
#   Note how Column B remains the same

def flipVertical(image):
    height = len(image[0])
    width = len(image)
    for x in range(width):
        for y in range(height//2):
            temp = image[x][y]
            image[x][y] = image[x][height-y-1]
            image[x][height-y-1] = temp
    return (image)

# Scan image to half the height (so as to not copy the manipulations back lmao)
# Get Height, Width, and then replace scanned pixel with opposite end pixel
# For example:
#    a b c               a b c
#   #######             #######
# a #1 2 3#           a #7 8 9#
# b #4 5 6#      =    b #4 5 6#
# c #7 8 9#           c #1 2 3#
#   #######             #######
#
#   Note how Row B remains the same

def flipHorizontal(image):
    height = len(image[0])
    width = len(image)
    for y in range(height):
        for x in range(width // 2):
            temp = image[x][y]
            image[x][y] = image[width - x - 1][y]
            image[width - x - 1][y] = temp
    return (image)



# Intermediate Functions

# Scan row in image
# Scan pixel in row
# First element in pixel list is Red, set to 0
def removeRed(image):
    for pixelRow in image:
        for pixel in pixelRow:
            pixel[0] = 0
    return image

# Scan row in image
# Scan pixel in row
# Second element in pixel list is Green, set to 0
def removeGreen(image):
    for pixelRow in image:
        for pixel in pixelRow:
            pixel[1] = 0
    return image

# Scan row in image
# Scan pixel in row
# Third element in pixel list is Blue, set to 0
def removeBlue(image):
    for pixelRow in image:
        for pixel in pixelRow:
            pixel[2] = 0
    return image

# Scan row in image
# Scan pixel in row
# Get average of elements in pixel (R/G/B)
# Set elements = Average
# Elements are the RGB values
def convToGrayscale(image):
    for pixelRow in image:
        for pixel in pixelRow:
            sumAvg = int((pixel[0]+pixel[1]+pixel[2])/3)
            for i in range(3):
                pixel[i] = sumAvg
    return image


# Scan pixels
# Apply Sepia Filter values provided in the document
# Set an upper limit to transformation (max 255)
# Replace RGB with new values
def applySepia(image):
    for pixelRow in image:
        for pixel in pixelRow:
            SepiaRed = int((pixel[0] * .393) + (pixel[1] * .769) + (pixel[2] * .189))
            SepiaGreen = int((pixel[0] * .349) + (pixel[1] * .686) + (pixel[2] * .168))
            SepiaBlue = int((pixel[0] * .272) + (pixel[1] * .534) + (pixel[2] * .131))

            if(SepiaRed > 255):
                SepiaRed = 255
            if(SepiaGreen > 255):
                SepiaGreen = 255
            if(SepiaBlue > 255):
                SepiaBlue = 255

            pixel[0] = SepiaRed
            pixel[1] = SepiaGreen
            pixel[2] = SepiaBlue
    return image


# Scan pixel
# If the individual RGB values are greater than / equal to 10, apply a decrement of 10
def decreaseBrightness(image):
    for pixelRow in image:
        for pixel in pixelRow:
            for i in range(3):
                if pixel[i]>=10:
                    pixel[i] = pixel[i]-10
    return image

# Scan pixel
# If the individual RGB values are less than / equal to 245, apply an increment of 10
def increaseBrightness(image):
    for pixelRow in image:
        for pixel in pixelRow:
            for i in range(3):
                if pixel[i]<=245:
                    pixel[i] = pixel[i] + 10
    return image

# Advanced Functions


def rotateLeft(image):
    new_image = list(zip(*image[::-1]))
    return(new_image)


def rotateRight(image):
    new_image = list(reversed(list(zip(*image))))
    return(new_image)


def pixelate(image):
    redTotal = 0
    greenTotal = 0
    blueTotal = 0
    height = len(image[0]) - len(image[0])%4
    width = len(image) - len(image)%4
    for y in range(0, height, 4):
        for x in range(0, width, 4):
            for i in range(4):
                for j in range(4):
                    redTotal += image[x+i][y+j][0]
                    greenTotal += image[x+i][y+j][1]
                    blueTotal += image[x+i][y+j][2]
            for i in range(4):
                for j in range(4):
                    image[x+i][y+j][0] = int(redTotal/16)
                    image[x+i][y+j][1] = int(greenTotal/16)
                    image[x+i][y+j][2] = int(blueTotal/16)
            redTotal = 0
            greenTotal = 0
            blueTotal = 0

    return (image)

def thresholdCalculator(image):

    height = len(image[0])
    width = len(image)

    totalRed = 0

    image = convToGrayscale(image)

    for pixelRow in image:
        for pixel in pixelRow:
            totalRed += pixel[0]

    redThreshold = int(totalRed / (height * width))

    backgroundThresholdTotal = 0
    foregroundThresholdTotal = 0
    backgroundCounter = 0
    foregroundCounter = 0
    newThreshold = 0

    test = 1

    while(test == 1):
        for pixelRow in image:
            for pixel in pixelRow:
                if pixel[0] > redThreshold:
                    backgroundThresholdTotal += pixel[0]
                    backgroundCounter += 1
                else:
                    foregroundThresholdTotal += pixel[0]
                    foregroundCounter += 1

        backgroundThreshold = int(backgroundThresholdTotal / backgroundCounter)
        foregroundThreshold = int(foregroundThresholdTotal / foregroundCounter)

        newThreshold = int((backgroundThreshold + foregroundThreshold) / 2)

        if(newThreshold - redThreshold < 10):
            test = 0

        backgroundThresholdTotal = 0
        foregroundThresholdTotal = 0
        backgroundCounter = 0
        foregroundCounter = 0

    return (newThreshold)


def binarize(image, threshold):
    convToGrayscale(image)
    for pixelRow in image:
        for pixel in pixelRow:
            if pixel[0] > threshold:
                for i in range(3):
                    pixel[i] = 255
            else:
                for i in range(3):
                    pixel[i] = 0
    return(image)





