from shared_data import window_width, window_height, ScreenMode
import shared_data
import pygame

class MainMenu(object):
    def __init__(self):
        self.background = pygame.transform.scale(
            pygame.image.load("Content/Images/Backgrounds/mainMenuBackground.jpg"), (window_width, window_height))

        # Setting up screen buttons

    def on_loop(self, window):
        self.update()
        self.draw(window)

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.background, (0, 0))