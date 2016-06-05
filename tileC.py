import pygame

class Tile(pygame.Rect):

	List = []
	width, height = 40, 40
	totalTiles = 1

	def __init__(self, x, y, Type):

		self.type = Type
		self.number = Tile.totalTiles
		Tile.totalTiles += 1

		if Type == 'empty':
			self.walkable = True
		else:
			self.walkable = False

		pygame.Rect.__init__(self, (x, y) , (Tile.width, Tile.height) )

		Tile.List.append(self)

	@staticmethod
	def get_tile(number):
		for tile in Tile.List:
			if tile.number == number:
				return tile

	@staticmethod
	def draw_tiles(screen):
		for tile in Tile.List:

			if not(tile.type == 'empty'):
				pygame.draw.rect(screen, [40, 40, 40], tile )