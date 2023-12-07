import pygame
import game_display
import time

pygame.init()

display_width = 500
display_height = 800
borderW = 50
borderH = 100

#color scheme
white = (255, 255, 255)
blue = (45, 56, 89)
purple = (168, 44, 131)
pink = (222, 0, 111)
red = (144, 12, 63)
light_pink = (248, 200, 220)
button_pink = (255, 224, 237)

deadCon = pygame.image.load("deadIcon.png")
deadIcon = pygame.transform.smoothscale(deadCon, (150, 150))

window = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()


class Screens(): #class that start, finished, and dead screen are made from
    pygame.mixer.music.load('jazz.mp3')
    pygame.mixer.music.play(-1)

    def __init__(self, messageText):
        self.messageText = messageText #defines the main text displayed on screen
        self.game_display = game_display.GameDisplay(display_width, display_height, window, clock, white, blue, purple, pink, red,light_pink)
     
    def message(self): #creates text box with main text
        messageFont = pygame.font.SysFont("stixgeneralbolita", 115) #main text font
        #checks if the message is short enough to fit on the screen
        if len(self.messageText) > 9: #if message is too long (number might need to change if font changes)
          messageTop, messageBottom = self.messageText.split(" ") #split message at space
          messageDispTop = messageFont.render(messageTop, True, blue) #create 2 seperate text boxes for message
          messageDispBottom = messageFont.render(messageBottom, True, blue)
          return messageDispTop, messageDispBottom 
        else: #message is right length
          messageDisp = messageFont.render(self.messageText, True, blue) #create text box
          return messageDisp

    def second_message(self):
        secondFont = pygame.font.SysFont("stixgeneralbolita", 45)
        secondDisp = secondFont.render("LEVEL COMPLETED", True, blue) #create text box
        return secondDisp

    def button(self, x, y, bText, bAction = None): #creates buttons
        self.x = x 
        self.y = y 
        self.bText = bText #text displayed in button
        self.bAction = bAction #what class button goes to if clicked

        mouse = pygame.mouse.get_pos() #tracks user's mouse position
        click = pygame.mouse.get_pressed() #listens for if the user clicks mouse

        if self.x+175 > mouse[0] > self.x and self.y+100 > mouse[1] > self.y: #if mouse hovers over button
            pygame.draw.rect(window, pink,(self.x,self.y,175,100)) #button turns pink
            if click[0] == 1 and self.bAction != None: #if mouse clicks
                self.bAction() #button runs defined class
        else: #regular button display
            #makes the box borders different color
            pygame.draw.rect(window, pink,(self.x,self.y+5,175,100), 5)
            pygame.draw.rect(window, blue, (self.x,self.y-5,175,100), 5)
            pygame.draw.rect(window, red, (self.x-5,self.y,175,100), 5)
            pygame.draw.rect(window, purple, (self.x+5,self.y,175,100), 5)
            pygame.draw.rect(window, button_pink,(self.x,self.y,175,100))
            
        bFont = pygame.font.SysFont("stixgeneralbolita",30) #defines button font
        buttonText = bFont.render(self.bText, True, blue) #creates button text box

        return buttonText 

    def dots(self): #draws dots
        if len(self.messageText) > 9: #draws dots for longer message
            pygame.draw.circle(window, pink, (460, (borderH/2)+30), 25)
            pygame.draw.circle(window, purple, (80, 240), 25)
            pygame.draw.circle(window, red, (350, 420), 25)
            pygame.draw.circle(window, blue, (30, 530), 25)
        else: #draws dots for shorter message
            mH = self.message().get_height() #defines height of message to center a dot
            pygame.draw.circle(window, pink, (460, (borderH/2)+30), 25)
            pygame.draw.circle(window, purple, (40, borderH+(mH/2)), 25)
            pygame.draw.circle(window, red, (350, 420), 25)
            pygame.draw.circle(window, blue, (30, 530), 25)

    def quitGame(self):
        pygame.quit()
        quit()

    def display(self):
        run = True #run is false when exit button or close button is pressed
        while run: #displays screen while run is true
            for event in pygame.event.get(): #sees if close button gets clicked
                if event.type == pygame.QUIT: #if so, exit game
                    run = False

            window.fill(light_pink) #background is light pink
            #checks if the message is short enough to fit on the screen
            if len(self.messageText) > 9: #if too long, display the 2 text boxes
                messageDispTop, messageDispBottom = self.message() #defines each text box from message method
                m1W = messageDispTop.get_width()
                m1H = messageDispTop.get_height()
                window.blit(messageDispTop, (10, borderH)) #displays top text box
                window.blit(messageDispBottom, (borderW*2, 250)) #displays bottom text box
                self.dots()
            else:
                #finds center of screen
                mW = self.message().get_width() 
                #defines x coordinate of message so text will be centered
                mX = (display_width-mW)/2
                window.blit(self.message(), (mX-2, borderH)) #displays centered text box
                if self.messageText == "OOPS":
                    window.blit(deadIcon, (mX+(mW/4), 250))
                else:
                    window.blit(self.second_message(), (40, 250))
                self.dots()

            #displays the 2 buttons
            window.blit(self.button(55, 575, "Restart", self.game_display.display), (93, 602))
            if self.messageText == "COLOR CRAZE":
                window.blit(self.button(55, 575, "Start Game", self.game_display.display), (66, 602))
            
            if game_display.finished_game:
                run = False
            
            if game_display.lost_game:
               run = False

            window.blit(self.button(275, 575, "Exit Game", self.quitGame), (294, 602))

            pygame.display.update()



