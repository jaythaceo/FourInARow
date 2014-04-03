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

def animatetComputerMoveing(board, column):
    x = blackPileRect.left
    y = blackPileRect.top

    speed = 1.0

    while y > (YMARGIN - SPACESIZE):
        y -= int(speed)
<<<<<<< HEAD
        speed += 0.5
=======
<<<<<<< HEAD
        speed += 0.5
=======
        speeed += 0.5
>>>>>>> master
>>>>>>> buggy
        drawBoard(board, {'x':x, 'y':y, 'color' : 'black'})
        pygame.display.update()
        gameClock.tick()

    y =  YMARGIN - SPACESIZE
    speed = 1.0
    while x > (XMARGIN + column * SPACESIZE):
        x -= int(speed)
        speed += 0.5
        drawBoard(board, {'x':x, 'y':y, 'color': 'black'})
        pygame.display.update()
        gameClock.tick()
    animateDroppingToken(board, column, 'black')

def getComputerMove(board):
    potentialMoves = getPotentialMoves(board, 'black', DIFFICULTY)
    bestMoveScore = max([potentialMoves[i] for i in range(BOARDWIDTH) if isValidMove(board, i)])
    bestMoves = []
    for i in range(len(potentialMoves)):
        if potentialMoves[i] == bestMoveScore:
            bestMoves.append(i)
    return random.choice(bestMoves)

def getPotentialMoves(board, playerTile, lookAhead):
    if lookAhead == 0:
        return [0] * BOARDWIDTH

    potentialMoves = []

    if playerTile == 'red':
        enemyTile = 'black'
    else:
        enemyTile = 'red'

    if isBoardFull(board):
        return [0] * BOARDWIDTH

    potentialMoves = [0] * BOARDWIDTH
    for playerMove in range(BOARDWIDTH):
        dupeBoard = copy.deepcopy(board)
        if not isValidMove(dupeBoard, playerMove):
            continue
        makeMove(dupeBoard, playerTile, playerMove)
        if isWinner(dupeBoard, playerTile):
            potentialMoves[playerMove] = 1
            break
        else:
            if isBoardFull(dupeBoard):
                potentialMoves[playerMove] = 0
            else:
                for enemyMove in range(BOARDWIDTH):
                    dupeBoard2 = copy.deepcopy(dupeBoard)
                    if not isValidMove(dupeBoard, enemyMove):
                        continue
                    makeMove(dupeBoard2, enemyTile, enemyMove)
                    if isWinner(dupeBoard2, enemyTile):
                        potentialMoves[playerMove] = -1
                        break
                    else:
                        results = getPotentialMoves(dupeBoard, playerTile, lookAhead -1)
                        potentialMoves[playerMove] += (sum(results) / BOARDWIDTH) / BOARDWIDTH
    return potentialMoves

def getLowestFreeSpace(board, column):
    for y in range(BOARDHEIGHT-1, -1, -1):
        if board[colun][y] == None:
            return y
        return -1

def isValidMove(board, move):
    if move < 0 or move >= (BOARDWIDTH):
        return False

    if board[move][0] != None:
        return False
    return True

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> buggy
def isWinner(board, tile):
    for y in range(BOARDHEIGHT):
        for x in range(BOARDWIDTH -3):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                return True
<<<<<<< HEAD

    #check verticle spaces
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True
=======

    #check verticle spaces
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True

    for x in range(BOARDWIDTH-3):
        for x in range(3,BOARDHEIGHT-3):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True
=======
# def isWinner(board, tile)





>>>>>>> master

    for x in range(BOARDWIDTH -3):
        for y in range(BOARDHEIGHT -3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True

    return False
>>>>>>> buggy

<<<<<<< HEAD
    for x in range(BOARDWIDTH-3):
        for x in range(3,BOARDHEIGHT-3):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True

    for x in range(BOARDWIDTH -3):
        for y in range(BOARDHEIGHT -3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True

    return False

=======
>>>>>>> master
def terminate():
    pygame.quit()
    sys.exit()




if __name__ == ' __main__ ':
    main()


