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
    
    def checkWin(self):
        # Function that checks if someone one
        # Returns True if someone one
        # Returns False if the status of a win doesn't apply
        # -----------------------------------
        # 
        
        
        #  Diagonals
        counter_0 = 0 # Counter for Main Diagonal, ('X')
        counter_01 = 0 # Counter for Main Diagonal, ('O')
        counter_1 = 0 # Counter for Secondary Diagonal, ('X') 
        counter_11 = 0 # Counter for Secondary Diagonal, ('O')
            
        aux = 2
        
        for x in range( 0 , 3):
            
            #  Rows and Columns
            count_0 = 0 # counter for row , ('X')
            count_1 = 0 # counter for row , ('O')
            count_01 = 0 # counter for col , ('X')
            count_11 = 0 # counter for col , ('O')
            
            
            for y in range( 0 , 3):
                
                # Check Rows
                if( self.__board[x][y] == self.__variables[0] ):
                    count_0 += 1
                elif( self.__board[x][y] == self.__variables[1] ):
                    count_1 += 1
                
                # Check Columns
                if( self.__board[y][x] == self.__variables[0] ):
                    count_01 += 1
                elif( self.__board[y][x] == self.__variables[1] ):
                    count_11 += 1
                    
            # Verification
            if( count_0 == 3 or count_1 == 3 or count_01 == 3 or count_11 == 3): 
                return True
            
            # Check Diagonals
            # Main Diagonal check
            if( self.__board[x][x] == self.__variables[0] ):
                counter_0 += 1
            elif( self.__board[x][x] == self.__variables[1] ):
                counter_1 += 1
                
            # Secondary diagonal
            if ( self.__board[x][aux] == self.__variables[0] ):
                counter_01 += 1
            elif( self.__board[x][aux] == self.__variables[1] ):
                counter_11 += 1
            
            # Verification
            if( counter_0 == 3 or counter_01 == 3 or counter_1 == 3 or counter_11 == 3 ):
                return True
            
            aux -= 1
            
        return False
            
    # Check if there are plays available
    def checkPlays(self):
        print("")
            
    # Check if movement it's available
    def checkMovement(self, row, col):
        # function that checks movement of the player on the board
        # returns True if the position it's clear
        # returns False if the position is already taken
        # -----------------------------------------
        # row : Row on the board 
        # col : Col on the board
        # ------------------------------------------
        #
        status = False
        if (row > 3 or row < 0 or col > 3 or col < 0):
            status = False
        else:
            if(self.__board[row][col] == None):
                status = True

        return status
    
    # Make the movement
    def doMovement(self, row, col):
        # function that does movement of the player on the board
        # returns True if it's successfull
        # returns False if it's unsuccessful
        # -----------------------------------------
        # row : Row on the board 
        # col : Col on the board
        # ------------------------------------------
        #
        if(not self.checkMovement(row, col)):
            return False
        else:
            self.__board[row][col] = self.__variables[0]
            return True

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
        
        #Variables
        surface = self.gameDisplay
        color = self.black
        center = ((self.size_x // 2) + (row * self.size_x), (self.size_y // 2) + (col * self.size_y))
        radius = ((self.size_x + self.size_y) // 4) - 5
        width = 20
        
        #Function to draw circle
        pygame.draw.circle(surface, color, center, radius, width)
        
    def drawRectangle(self, row, col):
        # Draws rectangle on the board at (row, col)
        # ------------------------------------------        
        # row : Row on the board 
        # col : Col on the board
        # ------------------------------------------
        # rect(surface, color, rect) -> Rect
        
        # Variables
        surface = self.gameDisplay
        color = self.dimgrey
        pos_x = row * (self.size_x + 5)
        pos_y = col * (self.size_y + 5)
        rect = pygame.Rect(pos_x, pos_y, self.size_x, self.size_y) # rectangle to draw, position and dimensions
        
        # Function to draw rectangle
        pygame.draw.rect(surface, color, rect)
    
    def drawX(self, row, col):
        # Draws 'X' on the board at (row, col)
        # ------------------------------------------        
        # row : Row on the board 
        # col : Col on the board
        # ------------------------------------------
        # aaline(surface, color, start_pos, end_pos, blend=1) -> Rect
        
        # Variables
        # ------------------------------------------
        # First Line \
        surface = self.gameDisplay
        color = self.black
        start_pos = (row * self.size_x,(col * self.size_y))
        end_pos = (row * self.size_x  + self.size_x, col * self.size_y + self.size_y)
        blend = 1
        
        # Function to Draw First Line \
        pygame.draw.aaline(surface, color, start_pos , end_pos , blend)
        
        #---------------------------------------------
        # Second line /
        start_pos = ( ( ( row + self.size_x ) + row * self.size_x ) , ( col * self.size_y ) )
        end_pos = ( row * self.size_x, col * self.size_y + self.size_y )
        
        # Function to Draw Second Line /
        pygame.draw.aaline(surface, color, start_pos , end_pos , blend)
        
    @property
    def handlerMouse(self):
        # Function that handles the mouse interaction
        # -------------------------------------------
        # Variables
        mouse_pos = pygame.mouse.get_pos()
        
        pos_x = mouse_pos[0]
        pos_y = mouse_pos[1]
        
        # Finding the col and row here the mouse was clicked
        for x in range( 0 , 3 ):
            for y in range( 0 , 3 ):
                if ( pos_x < ( ( x * self.size_x  ) + self.size_x ) ):
                    if ( pos_y < ( ( y * self.size_y ) + self.size_y ) ):
                       if ( self.game.doMovement( x , y ) ):
                            print ( "Player moved to ( {} , {} ) successfuly ".format( x , y ) )
                            self.drawBoard()
                            
                            if( self.game.checkWin() ):
                                print( "Player On! " )
                            
                            # Write a function that writes for the screen
                       else:
                            print ( "Position it's already fill!" )
                            
                       return
   
    def drawBoard(self):
        # Draw the board on the screen
        # --------------------------------
        # Variables
        board = self.game.board
        variables = self.game.variables
             
        # Going through the board   
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
