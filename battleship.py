# A test board that I will experiment with for my battleship game.
import random, pygame, sys
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480

CELLSIZE = 20
EMPTY = None

assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"

CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

WHITE =     (255, 255, 255)
BLACK =     (  0,   0,   0)
RED   =     (255,   0,   0)
GREEN =     (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR   = BLACK

def main():
	global DISPLAYSURF, BASICFONT

	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
	pygame.display.set_caption('Battleship')

	while True:
		runGame()
		
def runGame():
	mousex = 0
	mousey = 0

	board = initBoard()

	while True:
		mouseClicked = False

		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos	
				mouseClicked = True

		gridx, gridy = convertPixelToGridCoord(mousex, mousey)
	
		# insert your logic here
		# check if that cell is not already occupied
		location  = retrieveCellInfo(board, gridx, gridy)		

		if location == EMPTY and mouseClicked:
			# add a square piece
			addPieceToBoard(board, gridx, gridy)		 

			# draw the piece	
			drawPiece(board[gridx][gridy], gridx, gridy)
			
		drawGrid()
		pygame.display.update()
	
def drawPiece(piece, gridx, gridy):
	# convert it to pixel coord
	pixelx, pixely = convertGridToPixelCoord(gridx, gridy)

	cell = pygame.Rect(pixelx, pixely, CELLSIZE, CELLSIZE)

	pygame.draw.rect(DISPLAYSURF, piece, cell) 

def drawGrid():
	for x in range(0, WINDOWWIDTH, CELLSIZE):	# draw vertical line
		pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
	
	for y in range(0, WINDOWHEIGHT, CELLSIZE):
		pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

def checkForKeyPress():
	if len(pygame.event.get(QUIT)) > 0:
		terminate()

def convertPixelToGridCoord(pixelx, pixely):
	# Convert pixel coordinates to grid coordinates
	left = int(pixelx / CELLSIZE)

	top = int(pixely / CELLSIZE)

	return (left, top)

def convertGridToPixelCoord(gridx, gridy):
	# Convert grid coordinates to pixel coordinates
	left = gridx * CELLSIZE

	top = gridy * CELLSIZE

	return (left, top)

def retrieveCellInfo(board, x, y): 
	return board[x][y]

def addPieceToBoard(board, x, y):
	# create a piece tuple with a color
	piece = (DARKGRAY)

	# add it to board at (x,y)
	board[x][y] = piece

def initBoard():
	board = []

	for x in range(CELLWIDTH):
		column = []
		for y in range(CELLHEIGHT):
			column.append(EMPTY)
		
		board.append(column)

	return board

def terminate():
	pygame.quit()
	sys.exit()

if __name__== '__main__':
	main()	
