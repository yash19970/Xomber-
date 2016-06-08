import pygame, sys, functions
from tileC import Tile
from classes import *
from interaction import interaction
from A_Star import A_Star
from time import sleep

pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.mixer.music.load('Audio/zombie_theme.ogg')
pygame.mixer.music.play(-1) #-1 : iur music will replay again, never stops


screen = pygame.display.set_mode((704, 448)) # 32, 32

Tile.preInit(screen) #tiles are made using function.

clock = pygame.time.Clock()
FPS = 20
totalFrames = 0

 
dungeon = pygame.image.load('images/dungeon.jpg')
survivor = Survivor(32 * 2, 32 * 4)


while True:

    screen.blit(dungeon, (0,0) )

    Zombie.spawn(totalFrames, FPS)
    Zombie.update(screen,survivor)

    survivor.movement()
    Bullet.superMassiveJumbleLoop(screen)
    
    A_Star(screen, survivor, totalFrames, FPS)
    interaction(screen, survivor)   
    survivor.draw(screen)
    functions.text_to_screen(screen,'Health: {0}'.format(survivor.health),0,0)
    functions.text_to_screen(screen,'Score: {0}'.format(Zombie.counter),0,20)

    pygame.display.flip()
    clock.tick(FPS)
    totalFrames += 1   
    if survivor.health <=0 :
        sleep(2.5)
        screen.blit(pygame.image.load('images/dead.jpg'), (0,0))
        pygame.display.update() 
        break

