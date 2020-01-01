import pygame

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