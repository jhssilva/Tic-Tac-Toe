# Graphical Tic-Tac-Toe Game

# Some info on pygame
# https://www.pygame.org/docs/tut/ChimpLineByLine.html
# https://www.pygame.org/docs/tut/MakeGames.html
# https://www.pygame.org/docs/

# Pygame librarie
import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
gainsboro = (220,220,220)
dimgrey = (105,105,105)

weight = 800
height = 800
block_size = height / 3
gameExit = False


pygame.init() # Needs to init the pygame

gameDisplay = pygame.display.set_mode((weight,height)) # Set the window size
pygame.display.set_caption("Tic-Tac-Toe") # Set title of the window
gameDisplay.fill(gainsboro) # Fill the background with the color X
pygame.mouse.set_visible(True) # Function to set the mouse visible


for x in range(0 , 3):
    for y in range( 0, 3):
        rect = pygame.Rect(x * (block_size + 5), y * (block_size + 5), block_size, block_size)
        pygame.draw.rect(gameDisplay, dimgrey, rect)
        pygame.display.update() #To update the display
    
pygame.display.update() #To update the display



# Game Cicle
while not gameExit:
    for event in pygame.event.get(): # Get Events
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.mouse.get_pressed():
            mouse_pos = pygame.mouse.get_pos()
            print("Position = " , mouse_pos)
    
    #mouse_pos = pygame.mouse.get_pos()
    #print("Position = " , mouse_pos)
            
            
gameDisplay.fill(white) # Fill the background with the color X
pygame.display.update() #To update the display
