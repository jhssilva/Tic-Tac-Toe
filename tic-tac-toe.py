# Graphical Tic-Tac-Toe Game

# Some info on pygame
# https://www.pygame.org/docs/tut/ChimpLineByLine.html
# https://www.pygame.org/docs/tut/MakeGames.html
# https://www.pygame.org/docs/

# Pygame librarie
import os
import sys
import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')

class Game():

    run = True

    def __init__(self):
        super().__init__()
    
    # Next turn that will be against computer
    
    # Check win
    
    # Check if movement it's available
    
    # Make the movement
    

    @property
    def __del__(self):
        print("Finishing the game")

class Rect():
    __pos_x = 0
    __pos_y = 0
    __size_x = 0
    __size_y = 0
    __pygame_obj = None # Obj when it's printed on screen

    def __init__(self, pos_x, pos_y, size_x, size_y, pygame_obj):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__size_x = size_x
        self.__size_y = size_y
        self.__pygame_obj = pygame_obj
    
    @property
    def pos_x(self):
        return self.__pos_x
    
    @pos_x.setter
    def pos_x(self, pos_x):
        self.__pos_x = pos_x
        
    @property
    def pos_y(self):
        return self.__pos_y
    
    @pos_y.setter
    def pos_y(self, pos_y):
        self.__pos_y = pos_y
    
    @property
    def size_x(self):
        return self.__size_x
    
    @size_x.setter
    def size_x(self, size_x):
        self.__size_x = size_x

    @property
    def size_y(self):
        return self.__pos_x
    
    @size_y.setter
    def size_y(self, size_y):
        self.__size_y = size_y
        
    @property
    def pygame_obj(self):
        return __pygame_obj

    @pygame_obj.setter
    def pygame_obj(self, pygame_obj):
        self.__pygame_obj = pygame_obj
        
class Graphical():
    game = None # Variable that keeps the obj Game
    array_rect = [] # Array of Rectangles (To keep the data and position of them)
    gameDisplay = None  # Game Display
    run = True # Variable that keeps track if the game is running
    
    # Colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    gainsboro = (220,220,220)
    dimgrey = (105,105,105)
    
    # Dimensions
    weight = 800
    height = 800
    block_size = height / 3
    size_x = weight / 3
    size_y = height / 3

    def __init__(self):
        super().__init__()
        print("Graphical Started")
        self.game = Game()
        self.setScreen
        self.start
        
    @property
    def setScreen(self):
        pygame.init() # Needs to init the pygame
        self.gameDisplay = pygame.display.set_mode((weight,height)) # Set the window size
        pygame.display.set_caption("Tic-Tac-Toe") # Set title of the window
        self.gameDisplay.fill(self.gainsboro) # Fill the background with the color X
        pygame.mouse.set_visible(True) # Function to set the mouse visible
        
        for x in range(0, 3):
            for y in range(0, 3):
                size_x = self.size_x
                size_y = self.size_y
                pos_x = x * (size_x + 5)
                pos_y = y * (size_y + 5)
                         
                rect = pygame.Rect(pos_x, pos_y, size_x, size_y)
                self.array_rect.append(Rect(pos_x, pos_y, size_x, size_y, rect)) #Create object array
                pygame.draw.rect(self.gameDisplay, dimgrey, rect)
                pygame.display.update()  # To update the display
    
    @property
    def start(self):
        # Game Cicle
        while self.run:
            for event in pygame.event.get():  # Get Events
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONUP:
                    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
                    mouse_pos = pygame.mouse.get_pos()
                    if pressed1:
                        print("OI")
                   # if rect.collidepoint(mouse_pos) and pressed1:
                       # print("Test")
                    print("Position = ", mouse_pos)

def Console():
    def __init__(self):
        print("Aqui")

def menu():
    print("*** Menu Options ***")
    print("1 - Graphical game")
    print("2 - Console Game")
    print("0 - Exit")
    option = int(input("Option: "))

    if(option > 2 or option < 0):
        print("Choose a valid option")
    else:
        menuHandler(option)

def menuHandler(option):
    if(option == 0):
        global run
        run = False
        return
    elif(option == 1):  # Graphical
        print("Graphical Game Started")
        graph = Graphical()
    elif(option == 2):  # Console
        print("Console Game Started")
        console = Console()
    else:
        print("Option invalid!")

run = True

while(run):
    menu()
    
# gameDisplay.fill(white) # Fill the background with the color X
# pygame.display.update() #To update the display
