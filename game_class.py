from game_grid import Grid
from brick_types import *
import random
import pygame

class Game:
	def __init__(self):
		self.grid = Grid()
		self.bricks = [IBrick(), JBrick(), LBrick(), OBrick(), SBrick(), TBrick(), ZBrick()]
		self.current_brick = self.random_brick()
		self.next_brick = self.random_brick()
		self.game_over = False
		self.score = 0
		self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
		self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")
		self.rank_sound = pygame.mixer.Sound("Sounds/rank.ogg")

		self.game_theme = pygame.mixer.Sound("Sounds/music.ogg")
		self.game_theme.play(-1)

	def stop_bgm(self):
		self.game_theme.stop()

	def score_upd(self, lines_cleared, move_down_points):
		previous_score = self.score
		if lines_cleared == 1:
			self.score += 100
		elif lines_cleared == 2:
			self.score += 300
		elif lines_cleared == 3:
			self.score += 500
		self.score += move_down_points

		score_thresholds = [500, 1500, 3000, 5000, 8000]
		for threshold in score_thresholds:
			if previous_score < threshold <= self.score:
				if self.score >= threshold:
					self.rank_sound.play()


	def random_brick(self):
		if len(self.bricks) == 0:
			self.bricks = [IBrick(), JBrick(), LBrick(), OBrick(), SBrick(), TBrick(), ZBrick()]
		brick = random.choice(self.bricks)
		self.bricks.remove(brick)
		return brick

	def move_left(self):
		self.current_brick.move(0, -1)
		if self.brick_inside() == False or self.brick_fits() == False:
			self.current_brick.move(0, 1)

	def move_right(self):
		self.current_brick.move(0, 1)
		if self.brick_inside() == False or self.brick_fits() == False:
			self.current_brick.move(0, -1)

	def move_down(self):
		self.current_brick.move(1, 0)
		if self.brick_inside() == False or self.brick_fits() == False:
			self.current_brick.move(-1, 0)
			self.lock_brick()

	def lock_brick(self):
		tiles = self.current_brick.get_cell_positions()
		for position in tiles:
			self.grid.grid[position.row][position.column] = self.current_brick.id
		self.current_brick = self.next_brick
		self.next_brick = self.random_brick()
		rows_cleared = self.grid.clear_full_rows()
		if rows_cleared > 0:
			self.clear_sound.set_volume(0.4)
			self.clear_sound.play()
			self.score_upd(rows_cleared, 0)
		if self.brick_fits() == False:
			self.game_over = True

	def new_game(self):
		self.grid.reset()
		self.bricks = [IBrick(), JBrick(), LBrick(), OBrick(), SBrick(), TBrick(), ZBrick()]
		self.current_brick = self.random_brick()
		self.next_brick = self.random_brick()
		self.score = 0

	def brick_fits(self):
		tiles = self.current_brick.get_cell_positions()
		for tile in tiles:
			if self.grid.is_empty(tile.row, tile.column) == False:
				return False
		return True

	def rotate(self):
		self.current_brick.rotate()
		if self.brick_inside() == False or self.brick_fits() == False:
			self.current_brick.undo_rotation()
		else:
			self.rotate_sound.set_volume(0.4)
			self.rotate_sound.play()

	def brick_inside(self):
		tiles = self.current_brick.get_cell_positions()
		for tile in tiles:
			if self.grid.is_inside(tile.row, tile.column) == False:
				return False
		return True
	

	def draw(self, screen):
		self.grid.draw(screen)
		self.current_brick.draw(screen, 11, 11)

		if self.next_brick.id == 3:
			self.next_brick.draw(screen, 420, 483)   
		elif self.next_brick.id == 4:
			self.next_brick.draw(screen, 420, 470)   
		else:
			self.next_brick.draw(screen, 438, 470) 

	
		
		