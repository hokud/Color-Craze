import pygame
import random

class Player():
    def __init__(self, x_coord, y_coord, size, window, blue, purple, pink, red):
        self.x = x_coord
        self.y = y_coord
        self.size = size
        self.window = window
        self.blue = blue
        self.purple = purple
        self.pink = pink
        self.red = red
       
        colors = [self.blue, self.purple, self.pink, self.red]
        self.color = colors[random.randrange(0,4)]
    
    def display(self):
        pygame.draw.circle(self.window, self.color, (self.x, self.y), self.size)
    
    def move_up(self):
        self.y -= 2

    def move_down(self):
        self.y += 2
    
    def get_coord(self):
        return self.x, self.y