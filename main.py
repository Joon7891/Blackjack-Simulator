from enum import Enum
import main_menu
import game_screen
import settings_screen
import pygame
import card

# Enumerable for screen modes
class ScreenMode(Enum):
    MainMenu = 1
    Game = 2
    Settings = 3

class Game(object):
    window_width = 600
    window_height = 480

    def __init__(self):
        pygame.init()
        self.screen_mode = ScreenMode.MainMenu
        self.window = pygame.display.set_mode((Game.window_width, Game.window_height))
        pygame.display.set_caption("Blackjack Simulator")
        pygame.display.set_icon(pygame.image.load("Content/Images/Icon.jpg"))

        music = pygame.mixer.music.load("Content/Audio/Music/Memoir_Of_Summer.mp3")
        pygame.mixer.music.play(-1)

    def on_init(self):
        card.Card.load()

    def on_loop(self):
        pass

    def on_run(self):
        self.on_init()

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