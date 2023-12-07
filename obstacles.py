import pygame

class Obstacle(): #obstacle parent class 
    def __init__(self, window, blue, purple, pink, red):
        self.window = window
        self.blue = blue
        self.purple = purple
        self.pink = pink
        self.red = red
        self.current_color = ()
        self.current_color2 = ()
    
    def rotate(self): #obstacle rotate colors 
        current_time = pygame.time.get_ticks()
        mod_result = current_time % 6000
        if  0 <= mod_result < 1500:
            self.display(0)
        elif 1500 <= mod_result < 3000:
            self.display(1)
        elif 3000 <= mod_result < 4500:
            self.display(2)
        elif 4500 <= mod_result < 6000:
            self.display(3)


class ObstacleCircle(Obstacle): #circle obstacle 
    # draws the arcs of the circles in either blue, red, purple, or pink
    def display(self, start_index):
        i1 = start_index
        i2 = (i1 + 1) % 4
        i3 = (i2 + 1) % 4
        i4 = (i3 + 1) % 4
        colors = [self.blue, self.purple, self.pink, self.red]
        pygame.draw.arc(self.window, colors[i1], (123, 60, 250, 250), 0.785, 2.356, 27)
        self.current_color2 = colors[i1]
        pygame.draw.arc(self.window, colors[i2], (123, 60, 250, 250), 2.356, 3.927, 27)
        pygame.draw.arc(self.window, colors[i3], (123, 60, 250, 250), 3.927, 5.498, 27)
        self.current_color = colors[i3]
        pygame.draw.arc(self.window, colors[i4], (123, 60, 250, 250), 5.498, 0.785, 27)

        
class ObstacleLine(Obstacle): #line obstacle 
    def rotate(self): #obstacle rotate colors 
        current_time = pygame.time.get_ticks()
        mod_result = current_time % 7500
        if  0 <= mod_result < 1500:
            self.display(0)
        elif 1500 <= mod_result < 3000:
            self.display(1)
        elif 3000 <= mod_result < 4500:
            self.display(2)
        elif 4500 <= mod_result < 6000:
            self.display(3)
        elif 6000 <= mod_result < 7500:
            self.display(4)

    def display(self, start_index):
        i1 = start_index
        i2 = (i1 + 1) % 5
        i3 = (i2 + 1) % 5
        i4 = (i3 + 1) % 5
        i5 = (i4 + 1) % 5
        colors = [self.blue, self.red, self.purple, self.pink, self.red]
        pygame.draw.rect(self.window, colors[i1], (75, 390, 70, 30))
        pygame.draw.rect(self.window, colors[i2], (145, 390, 70, 30))
        pygame.draw.rect(self.window, colors[i3], (215, 390, 70, 30))
        self.current_color = colors[i3] 
        #print(current_color)
        pygame.draw.rect(self.window, colors[i4], (285, 390, 70, 30))
        pygame.draw.rect(self.window, colors[i5], (355, 390, 70, 30))


class ObstacleSquare(Obstacle): #square obstacle 
    def display(self, start_index):
        i1 = start_index
        i2 = (i1 + 1) % 4
        i3 = (i2 + 1) % 4
        i4 = (i3 + 1) % 4
        colors = [self.blue, self.red, self.purple, self.pink]
        pygame.draw.rect(self.window, colors[i1], (160, 650, 175, 30))
        self.current_color = colors[i1] 
        pygame.draw.rect(self.window, colors[i2], (310, 525, 30, 155))
        pygame.draw.rect(self.window, colors[i3], (160, 525, 180, 30)) 
        self.current_color2 = colors[i3]
        pygame.draw.rect(self.window, colors[i4], (160, 525, 30, 155))
        
        


