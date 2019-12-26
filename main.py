import pygame

screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Blackjack Simulator")
icon = pygame.image.load("Content/Images/Icon.jpg")
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False