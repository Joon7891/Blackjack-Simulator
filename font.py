import pygame

saved_fonts = {}

def get_font(path, size):
    if (path, size) in saved_fonts:
        print("Cached")
        return saved_fonts[(path, size)]

    print("Instance")
    saved_fonts[(path, size)] = pygame.font.Font(path, size)
    return saved_fonts[(path, size)]