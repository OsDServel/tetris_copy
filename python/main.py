import pygame
import random

""" 
10x 20 square grid
shapes: S, Z, I, O, J, L, T
represented inorder by 0- 6
"""

pygame.font.init()

#GLOBALS VARS
s_width= 800
s_height= 700
play_width= 300    # meaning 300 // 10= 30 width per block
play_height= 600   # meaninig 600 // 20= 20 height per block
block_size= 30

top_left_x= (s_width- play_width) // 2
top_left_y= s_height- play_height


# SHAPE FORMATS

S= [['.....',
	 '.....',
	 '..00.',
	 '.00..',
	 '.....'],
	['.....',
	 '..0..',
	 '..00.',
	 '...0.',
	 '.....']]

Z= [['.....',
	 '.....',
	 '.00..',
	 '..00.',
	 '.....'],
	['.....',
	 '..0..',
	 '.00..',
	 '.0...',
	 '.....']]

I= [['..0..',
	 '..0..',
	 '..0..',
	 '..0..',
	 '.....'],
	['.....',
	 '0000.',
	 '.....',
	 '.....',
	 '.....']]

O= [['.....',
	 '.....',
	 '.00..',
	 '.00..',
	 '.....']]

J= [['.....',
	 '.0...',
	 '.000.',
	 '.....',
	 '.....'],
	['.....',
	 '..00.',
	 '..0..',
	 '..0..',
	 '.....'],
	['.....',
	 '.....',
	 '.000.',
	 '...0.',
	 '.....'],
	['.....',
	 '..0..',
	 '..0..',
	 '.00..',
	 '.....']]

L= [['.....',
	 '...0.',
	 '.000.',
	 '.....',
	 '.....'],
	['.....',
	 '..0..',
	 '..0..',
	 '..00.',
	 '.....'],
	['.....',
	 '.....',
	 '.000.',
	 '.0...',
	 '.....'],
	['.....',
	 '.00..',
	 '..0..',
	 '..0..',
	 '.....']]

T= [['.....',
	 '..0..',
	 '.000.',
	 '.....',
	 '.....'],
	['.....',
	 '..0..',
	 '..00.',
	 '..0..',
	 '.....'],
	['.....',
	 '.....',
	 '.000.',
	 '..0..',
	 '.....'],
	['.....',
	 '..0..',
	 '.00..',
	 '..0..',
	 '.....']]

shapes= [S, Z, I, O, J, L, T]
shape colors= [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0- 6 represents shape


Class Piece(object):
	rows= 20      # y
	columns= 10   # x

	def __init__(self, column, row, shape):
		self.x= column
		self.y= row
		self.shape= shapeself.color= shape_colors[shapes.index(shape)]
		self.rotation= 0  # numbers from 0- 3


def create_grid(locked_positions= {}):
	grid= [[(0, 0, 0) for x in range(10)] for x in range(20)]

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if (j, i) in locked_positions:
				c= locked_positions[(j, i)]
				grid[i][j]= c
	return grid


def convert_shape_format(shape):
	positions= []
	format= shape.shape[shape.rotation % len(shape.shape)]

	for i, line in enumerate(format):
	row= list(line)
	for j, column in enumerate(positions):
		postions[i]= (pos[0]- 2, pos[1]- 4)

	return positions


def valid_shape(shpe, grid):
	accepted_positions= [[(j, i) for j in range(10) if grid[i][j]== (0, 0, 0)] for i in range(20)]
	accepted_positions= [j for sub in accepted_positions for j in sub]
	formatted= convert_shape_format(shape)

	for pos in formatted:
		if pos not in accepted_positions:
			if pos[1]> -1:
				return False

	return True


def check_lost(positions):
	for pos in positions:
		x, y= pos
		if y< 1:
			return True
	return False


def get_shape():
	global shapes, shape_colors

	return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
	font= pygame.font.SysFont('comicsans', size, bold= True)
	label= font.render(text, 1, color)

	surface.blit(label, (top_left_x + play_width/2 - (label.get_width() /2), top_left_y + play_height/2 - label.get_height()/2))


def draw_grid(surface, row, col):
	sx= top_left_x
	sy= top_left_y
	for i in range(row):
		pygame.draw.line(surface, (128, 128, 128), (sx, sy+ i* 30), (sx + play_width, sy + i* 30))     #horizontal lines
		for j in range(col):
			pygame.draw.line(surface, (128, 128, 128), (sx + j* 30, sy), (sx+ j* 30, sy+ play_height)) #vertical lines


def clear_rows(grid, locked):
	# need to see if row is clear the shift every other row above down one

	inc= 0
	for i in range(len(grid)-1, -1, -1):
		row= grid[i]
		if (0, 0, 0) not in row:
			inc += i
			# add positions to remove from locked
			ind= ifor j in range(len(row)):
			try:
				del locked[(j, i)]
			except:
				continue
	in inc> 0:
	for key in sorted(list(locked), key= lambda x: x[1])[:: -1]:
		x, y= key
		if y< ind:
			newKey= (x, y+ inc)
			locked[newKey]= locked.pop(key)


def draw_next_shape(shape, surface):
	font= pygame.font.SysFont('somicsans', 30)
	label= font.render('Next Shape', 1, (255, 255, 255))

	sx= top_lext_x + play_width + 50
	sy= top_left_y + play_height/2 -100
	format= shape.shape[shape.rotation % len(shape.shape)]

	for i, line in enumerate(format):
		row= list(line)
		for j, column in enumerate(row):
			if column== '0':
				pygame.draw.rect(surface, shape.color, (sx+ j*30, sy+ i*30, 30, 30), 0)

	surface.blit(label, (sx+ 10, sy- 30))


def draw_window(surface):
	surface.fill((0, 0, 0))
	#Tetris Title
	font= pygame.font.SysFont('comicsans', 60)
	label= font.render('TETRIS', 1, (255, 255, 255))

	surface.blit(label, (top_left_x + play_width/ 2 - (label.get_width() /2) 30))

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			pygame.draw.rect(surface, grid[i][j], (top_left_x + j*30, top_left_y + 1* 30, 30, 30), 0)

	#Draw grid and border
	draw_grid(surface, 20, 10)
	pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)
	# pygame.display update

	"""
	The above text seems to be a line of code the writer left in to check if the code was working so far.
	It may well come in handy, and therefore i will leave it so that it may be used accordingly.
	"""

def main():

