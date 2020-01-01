from shared_data import ScreenMode
from colour import get_rgb
import shared_data
import pygame

class Text(object):
    # Change colour to enum and have a map from enum to colour?
    def __init__(self, text, font, colour, center_x, center_y):
        self.text_surface = font.render(text, True, get_rgb[colour])
        rect = self.text_surface.get_rect()
        self.destination = (center_x - rect.width // 2, center_y - rect.height // 2)

    def draw(self, window):
        window.blit(self.text_surface, self.destination)

class Button(object):
    @staticmethod
    def load():
        Button.click_sound = pygame.mixer.Sound("Content/Audio/SoundEffects/buttonClick.wav")

    @staticmethod
    def set_main_menu():
        shared_data.screen_mode = ScreenMode.MainMenu

    @staticmethod
    def set_game_screen():
        shared_data.screen_mode = ScreenMode.Game

    @staticmethod
    def set_settings_screen():
        shared_data.screen_mode = ScreenMode.Settings

    def __init__(self, x, y, width, height, image, action):
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))
        self.action = action

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Playing button sound effect and initiating action
        if pygame.mouse.get_pressed()[0] and self.x <= mouse_x <= self.x + self.width \
                and self.y <= mouse_y <= self.y + self.height:
            Button.click_sound.play()
            self.action()

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))