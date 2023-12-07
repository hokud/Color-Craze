import pygame
import obstacles
import player

finished_game = False
lost_game = False

class GameDisplay():
    def __init__(self, display_width, display_height, window, clock, white, blue, purple, pink, red, light_pink):
        self.display_width = display_width
        self.display_height = display_height
        self.window = window
        self.clock = clock
        self.white = white
        self.blue = blue
        self.purple = purple
        self.pink = pink
        self.red = red
        self.light_pink = light_pink

        self.obstacle_circle = obstacles.ObstacleCircle(window, blue, purple, pink, red)
        self.obstacle_line = obstacles.ObstacleLine(window, blue, purple, pink, red)
        self.obstacle_square = obstacles.ObstacleSquare(window, blue, purple, pink, red)
        self.player = player.Player(250, 750, 20, window, blue, purple, pink, red)
        
   
    def display(self):   
        global finished_game
        global lost_game
        run = True 

        while run: #displays screen while run is true
            self.window.fill(self.light_pink)
            self.player.display()
            self.obstacle_circle.rotate()
            self.obstacle_line.rotate()
            self.obstacle_square.rotate()

            for event in pygame.event.get(): #sees if close button gets clicked
                if event.type == pygame.QUIT: #if so, exit game
                    run = False
            
            keys = pygame.key.get_pressed()  # Checking pressed keys
            if keys[pygame.K_UP]:
                self.player.move_up()
            if keys[pygame.K_DOWN]:
                self.player.move_down()

            player_coord = self.player.get_coord()
            #print(player_coord)
            if player_coord[1] <= 20:
                finished_game = True
                run = False
        
            if 630 <= player_coord[1] <= 699:
                if self.player.color !=  self.obstacle_square.current_color:
                    lost_game = True
                    run = False
            
            if 504 <= player_coord[1] <= 574:
                if self.player.color !=  self.obstacle_square.current_color2:
                    lost_game = True
                    run = False

            if 370 <= player_coord[1] <= 439:
                if self.player.color !=  self.obstacle_line.current_color:
                    lost_game = True
                    run = False

            if 260 <= player_coord[1] <= 323:
                if self.player.color !=  self.obstacle_circle.current_color:
                    lost_game = True
                    run = False
            
            if 41 <= player_coord[1] <= 106:
                if self.player.color !=  self.obstacle_circle.current_color2:
                    lost_game = True
                    run = False


            pygame.display.update()
            self.clock.tick(40)

           
            


