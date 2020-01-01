from shared_data import window_width, window_height
from gui import Text, Button
from colour import Colour
import shared_data
import pygame
import font

class MainMenu(object):
    def __init__(self):
        # Importing background image and fonts
        self.background = pygame.transform.scale(
            pygame.image.load("Content/Images/Backgrounds/mainMenuBackground.jpg"), (window_width, window_height))
        self.title_font = font.get_font('Content/Fonts/Voga-Medium.otf', 100)

        # Setting up on-screen text and buttons
        self.title_text = Text("Blackjack", self.title_font, Colour.Black, 300, 65)
        self.new_game_button = Button(200, 150, 200, 50,
                                      pygame.image.load("Content/Images/Sprites/Buttons/newGameButton.png"),
                                      Button.set_game_screen)
        self.load_game_button = Button(200, 210, 200, 50,
                                       pygame.image.load("Content/Images/Sprites/Buttons/loadGameButton.png"),
                                       Button.set_game_screen)
        self.settings_button = Button(200, 270, 200, 50,
                                      pygame.image.load("Content/Images/Sprites/Buttons/settingsButton.png"),
                                      Button.set_settings_screen)

    def on_loop(self, window):
        self.update()
        self.draw(window)

    def update(self):
        # Updating various on screen buttons
        self.new_game_button.update()
        self.load_game_button.update()
        self.settings_button.update()

    def draw(self, window):
        # Drawing background image, text, and buttons
        window.blit(self.background, (0, 0))
        self.title_text.draw(window)
        self.new_game_button.draw(window)
        self.load_game_button.draw(window)
        self.settings_button.draw(window)
