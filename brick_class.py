from colors_class import Colors
import pygame
from position_class import Position

class Brick:
	def __init__(self, id):
		self.id = id
		self.cells = {}
		self.cell_size = 30
		self.row_offset = 0
		self.column_offset = 0
		self.rotation = 0
		self.colors = Colors.get_cell_colors()

	def move(self, rows, columns):
		self.row_offset += rows
		self.column_offset += columns

	def get_cell_positions(self):
		tiles = self.cells[self.rotation]
		moved_tiles = []
		for position in tiles:
			position = Position(position.row + self.row_offset, position.column + self.column_offset)
			moved_tiles.append(position)
		return moved_tiles

	def rotate(self):
		self.rotation += 1
		if self.rotation == len(self.cells):
			self.rotation = 0

	def undo_rotation(self):
		self.rotation -= 1
		if self.rotation == -1:
			self.rotation = len(self.cells) - 1

	def draw(self, screen, offset_x, offset_y):
		tiles = self.get_cell_positions()
		for tile in tiles:
			tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size + 474, 
				offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)