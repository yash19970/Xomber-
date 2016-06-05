import pygame
def text_(screen, text, x,y,size=15
	,color=(255,255,255),font_type='arial'):
	try:
			text = str(text)
			font = pygame.font.SysFont(font_type, size)
			text = font.render(text,True,color)
			screen.blit(text,(x,y))
	except Exception, e:
			print('error, font not set')	
			raise e