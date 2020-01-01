from shared_data import window_width, window_height, ScreenMode
from gui import Text, Button
from colour import Colour
import shared_data
import pygame

class MainMenu(object):
    def __init__(self):
        # Importing background image and fonts
        self.background = pygame.transform.scale(
            pygame.image.load("Content/Images/Backgrounds/mainMenuBackground.jpg"), (window_width, window_height))
        self.title_font = pygame.font.Font('Content/Fonts/Voga-Medium.otf', 80)

        # Setting up on-screen text and buttons
        self.title_text = Text("Blackjack", self.title_font, Colour.Black, 300, 50)
        self.settings_button = Button(515, 335, 80, 60,
                                      pygame.image.load("Content/Images/Sprites/Buttons/settingButton.png"),
                                      Button.set_settings_screen)

    def on_loop(self, window):
        self.update()
        self.draw(window)

    def update(self):
        # Updating various on screen buttons
        self.settings_button.update()

    def draw(self, window):
        # Drawing background image, text, and buttons
        window.blit(self.background, (0, 0))
        self.title_text.draw(window)
        self.settings_button.draw(window)