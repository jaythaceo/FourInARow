# Graphical Four-In-A-Row ( Connect Four clone )
# By: Jason Brooks
# March 31, 2014
# Email: jaythaceo@gmail.com

import random
import copy
import sys
import pygame
from pygame.locals import *

BOARDWITH = 7   # How many spaces wide the board is
BOARDHEIGHT = 6 # How many spaces tall the board is

DIFFICULTY = 2  # How many moves to look ahead, > 2 usually takes to long to compute since it's exponential

SPACESIZE = 50
FPS = 30        # Frames per second
WINDOW_WIDTH = 640
WINDOWHEIGHT = 480

XMARGIN = int((WINDOW_WIDTH - BOARDWIDTH * SPACESIZE) / 2)  # Left to right
YMARGIN = int((WINDOWHEIGHT - BOARDHEIGHT * SPACESIZE) / 2) # Above below

BRIGHTBLUE = (0, 50, 255)
WHITE =  (255,255,255)

BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

redPileRect  = pygame.Rect(int(SPACESIZE / 2), WINDOWHEIGHT - int(3 * SPACESIZE / 2), SPACESIZE, SPACESIZE)
blackPileRect = pygame.Rect(WINDOW_WIDTH - int(3 * SPACESIZE / 2), WINDOWHEIGHT - int(3 * SPACESIZE / 2), SPACESIZE, SPACESIZE)


def main():
    global redTokenImg, blackTokenImg, boardImg, gameClock, windowSurf

    pygame.init()
    gameClock = pygame.time.Clock()
    windowSurf = pygame.display.set_mode((WINDOW_WIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Four in a Row')

    redTokenImg = pygame.image.load('4row_red.png')
    redTokenImg = pygame.transform.smoothscale(redTokenImg, (SPACESIZE, SPACESIZE))
    blackTokenImg = pygame.image.load('4row_black.png')
    blackTokenImg = pygame.transform.smoothscale(redTokenImg, (SPAECSIZE, SPAECSIZE))
    boardImg = pygame.image.load('4row_board.png')
    boardImg = pygame.transform.smoothscale(boardImg, (SPAECSIZE, SPACESIZE))

    bigFont = pygame.font.Font('freeanabold.ttf', 72)
    normalFont = pygame.font.Font('freeanabold.ttf', 24)

    gameOverSurf2 = normalFont.render('Click to start a new game.', 1, TEXTCOLOR)
    gameOverSurf2 = gameOverSurf2.get_rect()
    gameOverSurf.cente  = (int(WINDOW_WIDTH / 2), int(WINDOWHEIGHT / 2) + 50)

    isFirstGame = True

    while True:
        if isFirstGame:
            turn = 'computer'
            isFirstGame = False
        else:
            if random.randint(0, 1) == 0:
                turn = 'computer'
            else:
                turn = 'human'
        mainBoard = getNewBoard()








if __name__ == ' __main__ ':
    main()


