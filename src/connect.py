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
    boardImg = pygame.transform.smoothscale(boardImg, (SPACESIZE, SPACESIZE))

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

        while True:
            if turn == 'human':
                getHumanMove(mainBoard)
                if isWinner(mainBoard, 'red'):
                    winner - 'Human wins'
                    break
                turn = 'human'

            if isBoardFull(mainBoard):
                winner = 'Tie'
                break

            gameOverSurf = bigFont.render(winner, 1, TEXTCOLOR)
            gameOverRect = gameOverSurf.get_rect()
            gameOverRect.center = (int(WINDOW_WIDTH / 2 ), int(WINDOWHEIGHT / 2))

            newGame = False
            while True:
                if newGame:
                    break
                drawBoard(mainBoard)
                windowSurf.blit(gameOverSurf, gameOverRect)
                windowSurf.blit(gameOversurf2, gameOverRect2)
                pygame.display.update()
                gameClock.tick()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        terminate()
                    if event.type == MOUSEBUTTONUP:
                        newGame = True
                        break

def makeMove(board, player, column):
    lowest = getLowestFreeSpace(board, column)
    if lowest != -1:
        board[column][lowest] = player

def drawBoard(board, extraToken=None):
    windowSurf.fill(BGCOLOR)

    # Draw Tokens
    spaceRect = pygame.Rect(0,0, SPACESIZE, SPACESIZE)
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            spaceRect.topleft = (XMARGIN + (x * SPACESIZE), YMARGIN +(y * SPACESIZE))
            if board[x][y] == 'red':
                windowSurf.blit(redTokenImg, spaceRect)
            elif board[x][y] == 'black':
                windowSurf.blit(blackTokenImg, spaceRect)

    if extraToken != None:
        if extraToken['color'] == 'red':
            windowSurf.blit(redTokenImg, (extraToken['x'],extraToken['y'], SPACESIZE,SPACESIZE))
        elif extraToken['color'] == 'black':
            windowSurf.blit(blackTokenImg, (extraToken['x'],extraToken['y'], SPACESIZE,SPACESIZE))

    # Draw board over tokens
    for x in range(BOARDWIDTH):
        for y in range(BOARDWIDTH)  :
            spaceRect.topleft = (XMARGIN + ( x * SPACESIZE), YMARGIN + ( y * SPACESIZE))
            windowSurf.blit(boardImg, spaceRect)

    windowSurf.blit(redTokenImg, redPileRect)
    windowSurf.blit(blackTokenImg, blackPileRect)

def getNewBoard():
    board = []
    for x in range(BOARDWIDTH):
        board.append([None] * BOARDHEIGHT)
        return board

# getHumanBoard
def getHumanBoard(board):
    draggingToken = False
    tokenx, tokeny = None, none
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if not draggingToken and event.type == MOUSEBUTTONDOWN and redPileRect.collidepoint(event.pos):
                draggingToken = True
            if draggingToken and event.type == MOUSEMOTION:
                tokenx, tokeny = event.pos
            if draggingToken and event.type == MOUSEBUTTONUP:

                if tokeny < YMARGIN and tokenx > XMARGIN and tokenx < WINDOW_WIDTH - XMARGIN:
                    column = int((tokenx - XMARGIN)  /  SPACESIZE)
                    if isValidMove(board, column):
                        animateDroppingToken(board, column, 'red')
                        board[column][getLowestFreeSpace(board, column)] = 'red'
                        drawBoard(board)
                        pygame.display.update()
                        return
                tokenx, tokeny = None, None
                draggingToken = False
        if tokenx != None and tokeny != None:
            drawBoard(board, {'x':tokenx - int(SPACESIZE / 2), 'y':tokeny - inr(SPACESIZE / 2), 'color':'red'})
        else:
            drawBoard(board)

        pygame.display.update()
        gameClock.tick()














if __name__ == ' __main__ ':
    main()


