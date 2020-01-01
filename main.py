from shared_data import window_width, window_height, ScreenMode
from enum import Enum
import shared_data
import main_menu
import game_screen
import settings_screen
import pygame
import card

class Game(object):
    def __init__(self):
        # Initializing basic PyGame components
        pygame.init()
        self.window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Blackjack Simulator")
        pygame.display.set_icon(pygame.image.load("Content/Images/Icon.jpg"))

        # Loading and setting up background music
        music = pygame.mixer.music.load("Content/Audio/Music/Memoir_Of_Summer.mp3")
        pygame.mixer.music.play(-1)

        # Setting up various helper classes
        card.Card.load()
        self.main_menu = main_menu.MainMenu()
        self.game_screen = game_screen.GameScreen()
        self.settings_screen = settings_screen.SettingsScreen()

    def on_loop(self):
        # Clearing display
        self.window.fill((0, 0, 0))

        # Calling appropriate screen loop
        if shared_data.screen_mode == ScreenMode.MainMenu:
            self.main_menu.on_loop(self.window)
        elif shared_data.screen_mode == ScreenMode.Game:
            self.game_screen.on_loop(self.window)
        else:
            self.game_screen.on_loop(self.window)

        # Updating display window
        pygame.display.update()

    def on_run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.on_loop()

# Initializing game and starting game loop if main.py is main file
if __name__ == "__main__":
    game = Game()
    game.on_run()