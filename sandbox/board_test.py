# A simple 12 by 12 game board, used for later purposes.

import pygame, sys
from pygame.locals import *

# create the constants
BOARDWIDTH = 12 
BOARDHEIGHT = 12
TILESIZE = 50 
WINDOWWIDTH = 800 
WINDOWHEIGHT = 600 
FPS = 30
BLANK = None

#	 	R 	G	B
BLACK = 	(0,     0, 	0)
WHITE = 	(255, 255,    255)
BRIGHTBLUE = 	(0,    50,    255)
DARKTURQUOISE = (3,    54,     73)
GREEN = 	(0,   204,      0)

BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20

#XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
#YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

XMARGIN = 0
YMARGIN = 0
def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption('A Test Board')
	BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

	mainBoard = getStartingBoard()
	
	while True:	# main game loop
		slideTo = None # the direction the tile should slide

		drawBoard(mainBoard)

		checkForQuit()
		
		pygame.display.update()
	#	FPSCLOCK.tick(FPS)
def terminate():
	pygame.quit()
	sys.exit()

def checkForQuit():
	for event in pygame.event.get(QUIT):
		terminate()
	
def getStartingBoard():
	# Test: we will have only one tile or game piece move around the board.
	board = []
	counter = 0 

	for x in range(BOARDWIDTH):
		column = []
		for y in range(BOARDHEIGHT):
			column.append(counter)
			counter += 1
		board.append(column)

	# add '1' tile to top
	board[0][0] = 1 

	return board

def drawBoard(board):
	# color the board
	DISPLAYSURF.fill(BGCOLOR)

	for tilex in range(len(board)):
		for tiley in range(len(board[0])):
			if board[tilex][tiley]:
				drawTile(tilex, tiley, board[tilex][tiley])

	left, top = getLeftTopOfTile(0, 0)
	width = BOARDWIDTH * TILESIZE
	height = BOARDHEIGHT * TILESIZE

	pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)
	
def drawTile(tilex, tiley, number, adjx = 0, adjy = 0):
	left, top = getLeftTopOfTile(tilex, tiley)

	pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))

	textSurf = BASICFONT.render(str(number), True, TEXTCOLOR)
	textRect = textSurf.get_rect()
	textRect.center = left + int(TILESIZE / 2) + adjx, top + int(TILESIZE / 2) + adjy
	DISPLAYSURF.blit(textSurf, textRect)

def getLeftTopOfTile(tileX, tileY):
	left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
	top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)

	return (left, top)

if __name__ == '__main__':
	main()
	
