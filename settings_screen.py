from shared_data import window_width, window_height
from gui import Text, Button
import pygame

class SettingsScreen(object):
    def __init__(self):
        self.background = pygame.transform.scale(
            pygame.image.load("Content/Images/Backgrounds/settingsBackground.jpg"), (window_width, window_height))
        self.back_button = Button(5, 5, 40, 40,
                                  pygame.image.load("Content/Images/Sprites/Buttons/backButton.png"),
                                  Button.set_main_menu)

    def on_loop(self, window):
        self.update()
        self.draw(window)

    def update(self):
        self.back_button.update()

    def draw(self, window):
        window.blit(self.background, (0, 0))
        self.back_button.draw(window)