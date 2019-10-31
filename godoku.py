# Godoku Minigame 
# Author: Kathrin Betzenbichler 

# a godoku is a sudoku, only with letters instead of numbers

import pygame 
import sys
from pygame.locals import *

# a nested list with all the right Godoku characters 
SOLVEDGODOKU=[["a", "u", "s", "l", "b", "o", "t", "e", "k"], 
["b", "o", "k", "t", "e", "s", "u", "a", "l"], 
["t", "l", "e", "k", "u", "a", "s", "b", "o"], 
["o", "t", "l", "b", "s", "u", "a", "k", "e"], 
["e", "k", "a", "o", "t", "l", "b", "u", "s"], 
["s", "b", "u", "a", "k", "e", "l", "o", "t"], 
["l", "e", "o", "s", "a", "b", "k", "t", "u"], 
["u", "a", "t", "e", "l", "k", "o", "s", "b"], 
["k", "s", "b", "u", "o", "t", "e", "l", "a"]] 

# a nested list with the Godoku characters and some blank spaces, represented as empty strings
# this is how the Godoku is shown to the user
GODOKU=[["a", "u", "s", "l", "", "", "t", "e", ""], 
["", "o", "k", "t", "e", "s", "", "a", ""], 
["t", "", "e", "", "", "", "", "", ""], 
["", "", "l", "", "s", "", "", "", "e"], 
["", "", "", "o", "t", "l", "", "", ""], 
["s", "", "", "", "k", "e", "l", "", ""], 
["", "", "", "s", "", "", "k", "", "u"], 
["", "a", "", "e", "", "", "o", "s", ""], 
["", "s", "b", "", "", "t", "e", "l", "a"]] 


FPS=30 	# sets speed of program to 30 frames per second

WINDOWWIDTH=640 	# sets the size of window's width in pixels
WINDOWHEIGHT=480 	# sets the size of window's height in pixels

COLUMNS=9 	# number of columns
ROWS=9 		# number of rows

BOXSIZE=40 	# sets the size of one box in pixels
GAPSIZE=5 	# sets the size of the gaps between boxes in pixels


# this calculates the number of pixels on the side of the Godoku board, between board and window
XSIDE=int((WINDOWWIDTH-(COLUMNS*(BOXSIZE+GAPSIZE)))/2)
YSIDE=int((WINDOWHEIGHT-(ROWS*(BOXSIZE+GAPSIZE)))/2)


def godoku(): 
	'''main game'''

	global FPSCLOCK, DISPLAY, FONT

	pygame.init() 	# initializes pygame

	FPSCLOCK=pygame.time.Clock()	# sets the timer and stores the function call in a variable
	DISPLAY=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))	# sets the game surface
	
	mousex=0 	# sentry variables for the mouse coordinates
	mousey=0
	
	mouseClicked=False 	# sentry variable for mouse click option
	
	pygame.display.set_caption("Godoku Game") 		# sets caption of the game window
	FONT=pygame.font.Font('freesansbold.ttf', 20) 	# sets the basic font for the game
	
	running=True
	while running: 		# the main game loop
		
		keyEvent=None 	# clears the key event variable
			
		DISPLAY.fill((206, 177, 128))	# sets the game window surface color to some sand color
		
		drawBorder() 	# calls the function to draw the borders of the Godoku board
		drawBoard()		# calls the function to draw the Godoku board

		for event in pygame.event.get(): 	# catches all possible events in the game
			if event.type==QUIT: 	# QUIT is a pygame variable from the pygame.locals module
				running=False 		# quits the main game loop
				#westernCave() 		# continues with the western cave
			
			elif event.type==MOUSEBUTTONUP:		# is also a pygame variable 
				mousex, mousey=event.pos 		# with the mouse coordinates your current position can be defined
				mouseClicked=True 				# mouseClicked evaluates true once the MOUSEBUTTONUP event happened
			
			elif event.type==KEYUP: 	# is also a pygame variable
				keyEvent=event.key		# creates a variable for the key event once the KEYUP event happened
				
		boxx, boxy=getBox(mousex, mousey) 	# calls the function to get the right box you clicked on
		character=getText(mousex, mousey)	# calls the function to get the text of the box you clicked on
		
		if boxx!=None and boxy!=None and mouseClicked==True and character=="": 	# mouse was clicked on a specific box and the text of the box was an empty string
			instructions() 		# call the instructions function to display it 
				
			if keyEvent!=None: 
				new=pressedKey(keyEvent) 	# stores the returned string depending on the key you pressed in a variable through the function call
				if new==SOLVEDGODOKU[boxy][boxx]: 	# if the pressed key was the right one for the corresponding box, so the returned string matches
					GODOKU[boxy][boxx]=new 			# the list is updated with your input
				else:
					mouseClicked=False		# if you press no key mouseClicked evaluates False again so you can click another box
					continue			# starts again from the top of the game loop

		if GODOKU==SOLVEDGODOKU: 	# if all boxes are filled, so the updated list matches the list for the solved Godoku
			endScreen() 		# calls the endScreen function 
				
		pygame.display.update() # updates the shown display
		FPSCLOCK.tick(FPS) 		# causes the program to render at 30 FPS
		
		
def instructions(): 
	"""drawing a transparent rectangle with the instruction text shown on it"""
	
	instructionBox=pygame.draw.rect(DISPLAY, (206, 177, 128, 0), (XSIDE, WINDOWHEIGHT-YSIDE, COLUMNS*BOXSIZE, BOXSIZE)) 
	instruction=FONT.render("Press corresponding key to choose your input", True, (255, 255, 255)) 
	DISPLAY.blit(instruction, instructionBox) 	# displays the text over the rectangle
	
		
def pressedKey(key): 
	"""returns the right string depending on the key input"""
	
	if key==K_a:
		return "a"
	elif key==K_b:
		return "b"
	elif key==K_e:
		return "e"
	elif key==K_k:
		return "k"
	elif key==K_l:
		return "l"
	elif key==K_o:
		return "o"
	elif key==K_s:
		return "s"
	elif key==K_t:
		return "t"
	elif key==K_u:
		return "u"
	else:
		return ""

def drawBoard(): 
	"""draws the Godoku board with 9x9 rectangles (boxes) and the corresponding characters on it, taken from the tuple"""
	
	for boxx in range(COLUMNS): 	# for every box on the x side
		left=boxx*(BOXSIZE+GAPSIZE)+XSIDE 	# get the left coordinate for drawing the box
		for boxy in range(ROWS):  	# and for every box on the y side
			top=boxy*(BOXSIZE+GAPSIZE)+YSIDE 	# get the top coordinate for drawing the box
			
			textBox=pygame.draw.rect(DISPLAY, (255, 255, 255), (left, top, BOXSIZE, BOXSIZE))
			textSurf=FONT.render(GODOKU[boxy][boxx], True, (0, 0, 0))
			DISPLAY.blit(textSurf, textBox.center)		# displays the text over the boxes

	
def drawBorder(): 
	"""draws the borderlines for the board, on the outside of the whole Godoku board and also after 3 boxes"""
	
	thickness=5 	# sets thickness of the line 
	left=XSIDE-thickness/2 	# calculates the left coordinate 
	top=YSIDE-thickness/2	# and the top coordinate to begin with 
	width=(COLUMNS*BOXSIZE)+((COLUMNS-1)*GAPSIZE)+thickness 	# calculates the width of the board
	height=(ROWS*BOXSIZE)+((ROWS-1)*GAPSIZE)+thickness			# calculates the heigth of the board

	border=pygame.draw.lines(DISPLAY, (0, 0, 0), True, ((left, top), (left, top+height), (left+width, top+height), (left+width, top)), thickness)
	pygame.draw.line(DISPLAY, (0,0,0), (XSIDE+3*BOXSIZE+2*GAPSIZE+thickness/2, YSIDE), (XSIDE+3*BOXSIZE+2*GAPSIZE+thickness/2, top+height), thickness)
	pygame.draw.line(DISPLAY, (0,0,0), (XSIDE+6*BOXSIZE+5*GAPSIZE+thickness/2, YSIDE), (XSIDE+6*BOXSIZE+5*GAPSIZE+thickness/2, top+height), thickness)
	pygame.draw.line(DISPLAY, (0,0,0), (XSIDE, YSIDE+3*BOXSIZE+2*GAPSIZE+thickness/2), (left+width, YSIDE+3*BOXSIZE+2*GAPSIZE+thickness/2), thickness)
	pygame.draw.line(DISPLAY, (0,0,0), (XSIDE, YSIDE+6*BOXSIZE+5*GAPSIZE+thickness/2), (left+width, YSIDE+6*BOXSIZE+5*GAPSIZE+thickness/2), thickness)
	
	
	
def getBox(x, y): 
	"""returns the box you clicked on through coordinates"""
	
	for boxx in range(COLUMNS): 
		left=boxx*(BOXSIZE+GAPSIZE)+XSIDE
		for boxy in range(ROWS):  
			top=boxy*(BOXSIZE+GAPSIZE)+YSIDE
			
			boxRect=pygame.Rect(left, top, BOXSIZE, BOXSIZE)
			
			if boxRect.collidepoint(x, y): 
				return (boxx, boxy) 

	return (None, None) 


def getText(x, y): 
	"""returns the corresponding character of the box you clicked on through coordinates"""
	
	for boxx in range(COLUMNS): 
		left=boxx*(BOXSIZE+GAPSIZE)+XSIDE
		for boxy in range(ROWS):  
			top=boxy*(BOXSIZE+GAPSIZE)+YSIDE
			
			boxRect=pygame.Rect(left, top, BOXSIZE, BOXSIZE)
			character=GODOKU[boxy][boxx]
			
			if boxRect.collidepoint(x, y): 
				return character

	return None 

				
def endScreen(): 
	"""highlights some boxes with another background color to show the solution word"""

	for boxx in range(COLUMNS): 
		left=boxx*(BOXSIZE+GAPSIZE)+XSIDE
		for boxy in range(ROWS):  
			top=boxy*(BOXSIZE+GAPSIZE)+YSIDE
			
			if [boxy, boxx] in [[8,4], [7,5], [6,6], [5,7], [4,8]]: 	# these are the indeces for the solution characters in the tuple
				endBox=pygame.draw.rect(DISPLAY, (156, 68, 0), (left, top, BOXSIZE, BOXSIZE))
				endText=FONT.render(GODOKU[boxy][boxx], True, (0, 0, 0))
				DISPLAY.blit(endText, endBox.center)	# displays the text over the boxes

	
godoku() 
