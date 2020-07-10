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
    __run = True
    __board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    
    # Computer is the 'O' 
    # Human is the 'X'
    __variables = ["X","O"]

    def __init__(self):
        super().__init__()
        self.__run = True
        self.__board = [[None, None, None],
                    [None, None, None],
                    [None, None, None]]
        
    @property
    def board(self):
        return self.__board
    
    @board.setter
    def board(self, board):
        self.__board = board
    
    @property
    def variables(self):
        return self.__variables
    
    # Next turn that will be against computer
    
    # Check win
    def checkWin(self):
        print("d")
            
    # Check if movement it's available
    def checkMovement(self, row, col):
        status = False
        if (row > 3 or row < 0 or col > 3 or col < 0):
            status = False
        else:
            if(self.__board[row][col] == 0):
                status = True

        return status
    
    # Make the movement
    

    @property
    def __del__(self):
        print("Finishing the game")
        
class Graphical():
    game = None # Variable that keeps the obj Game
    array_rect = [] # Array of Rectangles (To keep the data and position of them)
    gameDisplay = None  # Game Display
    run = True # Variable that keeps track if the game is running
    
    # Colors in RGB
    white = (255, 255, 255)
    red = (255, 0, 0)
    gainsboro = (220,220,220)
    dimgrey = (105,105,105)
    black = (0, 0, 0)
    
    # Dimensions
    weight = 800
    height = 800
    size_x = weight // 3
    size_y = height // 3

    def __init__(self):
        super().__init__()
        print("Graphical Started")
        self.game = Game()
        self.initBoard
        self.start
        
    @property
    def initBoard(self):
        # initializes the board
        # --------------------------
        #
        
        pygame.init() # Needs to init the pygame
        self.gameDisplay = pygame.display.set_mode((self.weight,self.height)) # Set the window size
        pygame.display.set_caption("Tic-Tac-Toe") # Set title of the window
        self.gameDisplay.fill(self.gainsboro) # Fill the background with the color X
        pygame.mouse.set_visible(True) # Function to set the mouse visible
        self.drawBoard() #Initializes the board
              
    @property
    def start(self):
        # Game Cicle
        # ------------------------
        #
        
        while self.run:
            for event in pygame.event.get():  # Get Events
                if event.type == pygame.QUIT:
                    self.run = False
                    break
                if event.type == pygame.MOUSEBUTTONUP:
                    self.handlerMouse
        
    def drawCircle(self, row, col):
        # Draw Circle on the game Board at position (row, col)
        # ---------------------------------------------------
        # row : Row on the board 
        # col : Col on the board
        # ---------------------------------------------------
        # circle(surface, color, center, radius, width (optional)) -> Rect
        surface = self.gameDisplay
        color = self.black
        center = ((self.size_x // 2) + (row * self.size_x), (self.size_y // 2) + (col * self.size_y))
        radius = ((self.size_x + self.size_y) // 4) - 5
        width = 20
        
        pygame.draw.circle(surface, color, center, radius, width)
        
    def drawRectangle(self, row, col):
        # Draws rectangle on the board at (row, col)
        # ------------------------------------------        
        # row : Row on the board 
        # col : Col on the board
        # ------------------------------------------
        
        pos_x = row * (self.size_x + 5)
        pos_y = col * (self.size_y + 5)
        rect = pygame.Rect(pos_x, pos_y, self.size_x, self.size_y)
        pygame.draw.rect(self.gameDisplay, self.dimgrey, rect)
    
    def drawX(self, row, col):
        # Draws 'X' on the board at (row, col)
        # ------------------------------------------        
        # row : Row on the board 
        # col : Col on the board
        # ------------------------------------------
        # aaline(surface, color, start_pos, end_pos, blend=1) -> Rect
        surface = self.gameDisplay
        color = self.black
        start_pos = (row * self.size_x,(col * self.size_y))
        end_pos = (row * self.size_x  + self.size_x, col * self.size_y + self.size_y)
        blend = 1
        pygame.draw.aaline(surface, color, start_pos , end_pos , blend)
    
    @property
    def handlerMouse(self):
        # Function that handles the mouse interaction
        # -------------------------------------------
        mouse_pos = pygame.mouse.get_pos()

        print("Position = ", mouse_pos)
    
    def drawBoard(self):
        # Draw the board on the screen
        # --------------------------------
        #
        board = self.game.board
        variables = self.game.variables
        
        #board[0][0] = 'X'
        board[0][1] = 'O'
        board[1][1] = 'X'
        print(board)
        
        for x in range(0 , 3):
            for y in range(0, 3):
                # Draw Grid
                self.drawRectangle(x, y)
                # Draw options selected on the board
                if(board[x][y] == variables[0]): # Variables[0] it's equal to 'X' 
                    self.drawX(x,y)
                elif(board[x][y] == variables[1]): # I'ts equal to 'O'
                    self.drawCircle(x,y)
            pygame.display.update()  # update the display          
    
    def __del__(self):
        self.gameDisplay.fill(self.white) # Fill the background with the color X
        pygame.display.update()  # To update the display
        pygame.display.quit()
        pygame.quit()

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
        graph = Graphical()
    elif(option == 2):  # Console
        console = Console()
    else:
        print("Option invalid!")

run = True

Graphical()


#while(run):
 #   menu()
    
# gameDisplay.fill(white) # Fill the background with the color X
# pygame.display.update() #To update the display
