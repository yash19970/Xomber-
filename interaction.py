import pygame, sys
from tileC import Tile
from classes import *
def interaction(screen, survivor):


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:
                survivor.current += 1
                survivor.current %= 3
                #always remains 0-2


    keys = pygame.key.get_pressed()



    if keys[pygame.K_w]: # North
        futureTileNumber = survivor.getNumber() - Tile.V
        if futureTileNumber in range(1, Tile.totalTiles + 1):
            futureTile = Tile.getTile(futureTileNumber)
            if futureTile.walkable:
                survivor.setTarget(futureTile)
                survivor.rotate('n')
                # survivor.y -= survivor.height                   

    if keys[pygame.K_s]: # South
        futureTileNumber = survivor.getNumber() + Tile.V
        if futureTileNumber in range(1, Tile.totalTiles + 1):
            futureTile = Tile.getTile(futureTileNumber)
            if futureTile.walkable:
                survivor.setTarget(futureTile)
                survivor.rotate('s')
                # survivor.y += survivor.height 

    if keys[pygame.K_a]: # West
        futureTileNumber = survivor.getNumber() - Tile.H

        if futureTileNumber in range(1, Tile.totalTiles + 1):
            futureTile = Tile.getTile(futureTileNumber)    
            if futureTile.walkable:
                survivor.setTarget(futureTile)
                survivor.rotate('w')
                # survivor.x -= survivor.width 

    if keys[pygame.K_d]: # East
        futureTileNumber = survivor.getNumber() + Tile.H
        if futureTileNumber in range(1, Tile.totalTiles + 1):
            futureTile = Tile.getTile(futureTileNumber)
            if futureTile.walkable:
                survivor.setTarget(futureTile)
                survivor.rotate('e')
                # survivor.x += survivor.width 

    if keys[pygame.K_LEFT]:
        survivor.rotate('w') #rorate west
        Bullet(survivor.centerx,survivor.centery, -10,0,'w',survivor.getBulletType())

    elif keys[pygame.K_RIGHT]:
        survivor.rotate('e')
        Bullet(survivor.centerx,survivor.centery, 10,0,'e',survivor.getBulletType())


    elif keys[pygame.K_UP]:
        survivor.rotate('n')
        Bullet(survivor.centerx,survivor.centery, 0,-10,'n',survivor.getBulletType())


    elif keys[pygame.K_DOWN]:
        survivor.rotate('s')
        Bullet(survivor.centerx,survivor.centery, 0,10,'s',survivor.getBulletType())

