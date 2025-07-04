# myColourModule.py
#
# Description: Contains functions related to pixels and their colour.
#
# Date: 2024

def isPixelGreen(r, g, b):
    ''' Function that returns True when pixel is green,
        otherwise, False. '''

    # A pixel is considered green if green is strong and dominant,
    # and red/blue are low.
    return g > 150 and r < 120 and b < 120

# Define a function to detect yellow pixels
def isPixelYellow(R, G, B):
    ''' Returns True if the given pixel is yellow, otherwise False. '''
    return R > 150 and G > 150 and B < 100
