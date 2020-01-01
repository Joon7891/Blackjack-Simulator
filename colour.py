from enum import Enum

# Enumerable to contain basic RBG colours
class Colour(Enum):
    Black = 1
    White = 2
    Red = 3
    Lime = 4
    Blue = 5
    Yellow = 6
    Cyan = 7
    Magenta = 8
    Silver = 9
    Gray = 10
    Maroon = 11
    Olive = 12
    Green = 13
    Purple = 14
    Teal = 15
    Navy = 16

# Dictionary to map Colour enum to corresponding RGB value
get_rgb = {
    Colour.Black: (0, 0, 0),
    Colour.White: (255, 255, 255),
    Colour.Red: (255, 0, 0),
    Colour.Lime: (0, 255, 0),
    Colour.Blue: (0, 0, 255),
    Colour.Yellow: (255, 255, 0),
    Colour.Cyan: (0, 255, 255),
    Colour.Magenta: (255, 0, 255),
    Colour.Silver: (192, 192, 192),
    Colour.Gray: (128, 128, 128),
    Colour.Maroon: (128, 0, 0),
    Colour.Olive: (128, 128, 0),
    Colour.Green: (0, 128, 0),
    Colour.Purple: (128, 0, 128),
    Colour.Teal: (0, 128, 128),
    Colour.Navy: (0, 0, 128),
}