import pygame
import screens
import game_display

gameIcon = pygame.image.load('gameIcon.png')
pygame.display.set_icon(gameIcon)

def run_screens():
    while True:
        # Create a new instance of Screens for each iteration
        start = screens.Screens("COLOR CRAZE")
        start.display()

        if game_display.finished_game:
            game_display.finished_game = False
            finished = screens.Screens("YAY!!")
            finished.display()

        if game_display.lost_game:
            game_display.lost_game = False
            dead = screens.Screens("OOPS")
            dead.display()

# Call the function to start the game loop
run_screens()