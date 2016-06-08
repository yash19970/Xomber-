import pygame
from tileC import Tile


class Character(pygame.Rect):
    width, height = 40, 40

    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, Character.width, Character.height)

    def __str__(self):
        return str(self.getNumber())

    def getNumber(self):
        return ((self.x / self.width) + Tile.H) + ((self.y / self.height) * Tile.V)

    def getTile(self):
        return Tile.getTile(self.getNumber())


class Zombie(Character):
    List = []
    def __init__(self, x, y):
        Character.__init__(self, x, y)
        Zombie.List.append(self)

    @staticmethod
    def drawZombies(screen):
        for zombie in Zombie.List:
            pygame.draw.rect(screen, [210, 24, 77], zombie)


class Survivor(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y)

    def draw(self, screen):
        r = self.width / 2
        pygame.draw.circle(screen, [77, 234, 156], (self.x + r, self.y + r), r)