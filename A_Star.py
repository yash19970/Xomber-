import pygame
from classes import *
from tileC import Tile

def A_Star(screen, survivor, totalFrames, FPS):
    
    half = Tile.width / 2

    N = -22
    S = 22
    E = 1
    W = -1

    NW = -23
    NE = -21
    SE = 23
    SW = 21

    for tile in Tile.List:
        tile.parent = None
        tile.H, tile.G, tile.F = 0,0,0

    def blocky(tiles, diagonals, surroundingNode):
        if surroundingNode.number not in diagonals:
            tiles.append(surroundingNode)
        return tiles

    def getSurroundingTiles(base_node):
        
        array =(
            (base_node.number + N),
            (base_node.number + NE),
            (base_node.number + E),
            (base_node.number + SE),
            (base_node.number + S),
            (base_node.number + SW),
            (base_node.number + W),
            (base_node.number + NW),
            )

        tiles = []

        onn = base_node.number 
        diagonals = [onn + NE, onn + NW, onn + SE, onn + SW]

        for tile_number in array:

            surroundingTile = Tile.getTile(tile_number)
            
            if tile_number not in range(1, Tile.totalTiles + 1):
                continue

            if surroundingTile.walkable and surroundingTile not in closedList:
                # tiles.append(surroundingTile) # Diagonal movement
                tiles = blocky(tiles, diagonals, surroundingTile)

        return tiles

    def G(tile):
        
        diff = tile.number - tile.parent.number

        if diff in (N, S, E, W):
            tile.G = tile.parent.G + 10
        elif diff in (NE, NW, SW, SE):
            tile.G = tile.parent.G + 14

    def H():
        for tile in Tile.List:
            tile.H = 10 * (abs(tile.x - survivor.x) + abs(tile.y - survivor.y)) / Tile.width

    def F(tile):
        # F = G + H
        tile.F = tile.G + tile.H

    def swap(tile):
        openList.remove(tile)
        closedList.append(tile)

    def getLFT(): # get Lowest F Value

        F_Values = []
        for tile in openList:
            F_Values.append(tile.F)

        o = openList[::-1]

        for tile in o:
            if tile.F == min(F_Values):
                return tile

    def move_to_G_cost(LFT, tile):

        GVal = 0
        diff = LFT.number - tile.number

        if diff in (N, S, E, W):
            GVal = LFT.G + 10
        elif diff in (NE, NW, SE, SW):
            GVal = LFT.G + 14

        return GVal

    def loop():

        LFT = getLFT() 

        swap(LFT)
        surroundingNodes = getSurroundingTiles(LFT)

        for node in surroundingNodes:

            if node not in openList:

                openList.append(node)
                node.parent = LFT

            elif node in openList:
                
                calculated_G = move_to_G_cost(LFT, node)
                if calculated_G < node.G:

                    node.parent = LFT
                    G(node)
                    F(node)

        if openList == [] or survivor.getTile() in closedList:
            return

        for node in openList:
            G(node)
            F(node)

            # pygame.draw.line(screen, [255, 0, 0],
            # [node.parent.x + half, node.parent.y + half],
            # [node.x + half, node.y + half] )

        loop()

        

    for zombie in Zombie.List:

        if zombie.tx != None or zombie.ty != None:
            continue

        openList = []
        closedList = []

        zombie_tile = zombie.getTile()
        openList.append(zombie_tile)

        surroundingNodes = getSurroundingTiles(zombie_tile)

        for node in surroundingNodes:
            node.parent = zombie_tile
            openList.append(node)      

        swap(zombie_tile)

        H()

        for node in surroundingNodes:
            G(node)
            F(node) 

        loop()

        returnTiles = []

        parent = survivor.getTile()

        while True:

            returnTiles.append(parent)

            parent = parent.parent

            if parent == None:
                break

            if parent.number == zombie.getNumber():
                break
                
        if len(returnTiles) > 1:
            next_tile = returnTiles[-1]
            zombie.setTarget(next_tile)