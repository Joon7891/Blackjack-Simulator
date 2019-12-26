import pygame


# Initializing components
pygame.init()
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Blackjack Simulator")
pygame.display.set_icon(pygame.image.load("Content/Images/Icon.jpg"))

# Background Music
music = pygame.mixer.music.load("Content/Audio/Music/Memoir_Of_Summer.mp3")
pygame.mixer.music.play(-1)

# Method to encapsulate game loop
def loop():

    # Clearing screen and updating game
    screen.fill((0, 0, 0))
    pygame.display.update()

# Initializing game and starting game loop if main.py is main file
if __name__ == "__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        loop()