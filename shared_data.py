from enum import Enum

# Enumerable for screen modes
class ScreenMode(Enum):
    MainMenu = 1
    Game = 2
    Settings = 3
screen_mode = ScreenMode.MainMenu

# Game window size
window_width = 600
window_height = 400