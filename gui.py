from colour import get_rgb
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
    def __init__(self, x, y, width, height, image, func):
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))
        self.func = func

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] and self.x <= mouse_x <= self.x + self.width \
                and self.y <= mouse_y <= self.y + self.height:
            func()

    def draw(self, window):
        window.blit(image, (self.x, self.y))