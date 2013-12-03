# Another test board using rectangle objects instead of lines
import random, pygame, sys
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480

CELLSIZE = 20
EMPTY = None

assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."

CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

WHITE = 	(255,255,255)
BLACK = 	(  0,  0,  0)
RED   = 	(255,  0,  0)
GREEN = 	(  0,255,  0)
DARKGREEN = 	(  0,155,  0)
DARKGRAY  =     ( 40, 40, 40)
BLUE      =     (  0,  0,255)
BGCOLOR = BLACK
HIGHTLIGHTCOLOR = BLUE

# Types of ships
BOAT = {'ROW': 2, 'COLUMN':2, 'COLOR':RED, 'NAME':'Boat'}

PIECES = (BOAT)

def main():
	global DISPLAYSURF, BASICFONT

	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	BASICFONT   = pygame.font.Font('freesansbold.ttf', 18)
	pygame.display.set_caption('Battleship')

	while True:
		runGame()

def runGame():
	mousex = 0
	mousey = 0

	board = initBoard()
	
	#drawBoard()
	#drawGrid()
	
	while True:
		DISPLAYSURF.fill(BLUE)	
		mouseClicked = False
		
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == MOUSEMOTION:
				mousex, mousey = event.pos		
			if event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
	
		gridx, gridy = convertPixelToGridCoord(mousex, mousey)
		
		location = retrieveCellInfo(board, gridx, gridy)
		
		if location == EMPTY:
			if mouseClicked:
				# add a boat piece
				addPieceToBoard(board, PIECES, gridx, gridy) 
				
			highlightCell(PIECES, gridx, gridy)
			
		drawGrid()
		updateBoardInfo(board)
		pygame.display.update()
		
		unhighlightCell(PIECES, gridx, gridy)

def updateBoardInfo(board):
	for x in range(0, CELLWIDTH):
		for y in range(0, CELLHEIGHT):
			if board[x][y] != EMPTY:
				# retrieve ship at x,y
				ship = board[x][y]
		
				# retrieve ship color at x,y
				color = ship['COLOR']
			
				(pixelx, pixely) = convertGridToPixelCoord(x, y)
			
				# draw the ship into the surface
				cell = pygame.Rect(pixelx, pixely, CELLSIZE, CELLSIZE)

				pygame.draw.rect(DISPLAYSURF, color, cell)

def checkBoardLocation(board, shipPiece, gridx, gridy):
	# check if board location is occupied by another ship
	pieceRow = shipPiece['ROW']

	pieceColumn = shipPiece['COLUMN']

	# out of bounds checkings
	if (gridx + 1) - pieceRow < 0 or (gridy + 1) - pieceColumn < 0:
		return False

	# cell occupied Checkings
	for x in range(gridx, gridx - pieceRow, -1):
		for y in range(gridy, gridy - pieceColumn, -1):
			if board[x][y] != None:
				return False
	return True

def addPieceToBoard(board, shipPiece, gridx, gridy):
	# add it to board at (x,y)

	# retrieve # of rows
	pieceRow = shipPiece['ROW']

	# retrieve # of columns
	pieceColumn = shipPiece['COLUMN']

	# valid placement
	err = checkBoardLocation(board, shipPiece, gridx, gridy)

	if (err):
		for x in range(gridx, gridx - pieceRow, -1):
			for y in range(gridy, gridy - pieceColumn, -1):
				board[x][y] = shipPiece

def highlightCell(shipPiece, gridx, gridy):
	pieceRow = shipPiece['ROW']

	pieceColumn = shipPiece['COLUMN']	

	for x in range(gridx, gridx - pieceRow, -1):
		for y in range(gridy, gridy - pieceColumn, -1):
			pixelx, pixely = convertGridToPixelCoord(x, y)

			cell = pygame.Rect(pixelx, pixely, CELLSIZE, CELLSIZE)

			pygame.draw.rect(DISPLAYSURF, RED, cell)	

def unhighlightCell(shipPiece, gridx, gridy):
	pieceRow = shipPiece['ROW']

	pieceColumn = shipPiece['COLUMN']	

	for x in range(gridx, gridx - pieceRow, -1):
		for y in range(gridy, gridy - pieceColumn, -1):
			pixelx, pixely = convertGridToPixelCoord(x, y)

			cell = pygame.Rect(pixelx, pixely, CELLSIZE, CELLSIZE)

			pygame.draw.rect(DISPLAYSURF, BLUE, cell)	

def retrieveCellInfo(board, x, y):
	return board[x][y]

def initBoard():
	board = []
	
	for x in range(CELLWIDTH):
		column = []
		for y in range(CELLHEIGHT):
			column.append(EMPTY)

		board.append(column)

	return board

def convertPixelToGridCoord(pixelx, pixely):
	# Convert pixel coordinates to grid coordinates
	left =  int(pixelx / CELLSIZE)

	top = int(pixely / CELLSIZE)

	return (left, top)

def convertGridToPixelCoord(gridx, gridy):
	# Convert grid coordinates to pixel coordinates
	left = gridx * CELLSIZE

	top = gridy * CELLSIZE

	return (left, top)

def drawBoard():
	for x in range(0, WINDOWWIDTH):
		for y in range(0, WINDOWHEIGHT):
			pixelx, pixely = convertGridToPixelCoord(x, y)

			# Create a cell
			cell = pygame.Rect(pixelx, pixely, CELLSIZE, CELLSIZE)
			
			# Create  a border
			pygame.draw.rect(DISPLAYSURF, BLUE, cell)

def drawGrid():
	for x in range(0, WINDOWWIDTH, CELLSIZE):
		pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))

	for y in range(0, WINDOWHEIGHT, CELLSIZE):
		pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

def terminate():
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()
