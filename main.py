import pygame, sys
from tileC import Tile
import functions 
pygame.init()
pygame.font.init()

invalids = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
			37,55,73,91,109,127,145,163,181,182,183,185,186,
			187,188,189,190,191,192,193,194,195,196,197,198,
			36,54,72,90,108,126,144,162,180,198)

screen = pygame.display.set_mode((720, 440))
for y in range(0,screen.get_height(), 40):
	for x in range(0,screen.get_width(), 40):
		
		if Tile.totalTiles in invalids:
			Tile(x, y, 'solid')
		else:
			Tile(x, y, 'empty')


clock = pygame.time.Clock()
FPS = 24 
total_frames = 0

 
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    	    sys.exit()

    Tile.draw_tiles(screen)
    #screen.fill([0,0,0])
    functions.text_(screen, 'funky', 250,300)
    pygame.display.flip()
    clock.tick(FPS)
    total_frames += 1