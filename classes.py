import pygame
from tileC import Tile
from random import randint 

class Character(pygame.Rect):

    width, height = 32, 32

    def __init__(self, x, y):

        self.tx, self.ty = None, None
        pygame.Rect.__init__(self, x, y, Character.width, Character.height)

    def __str__(self):
        return str(self.getNumber())

    def setTarget(self, next_tile):
        if self.tx == None and self.ty == None:
            self.tx = next_tile.x
            self.ty = next_tile.y

    def getNumber(self):
        
        return ((self.x / self.width) + Tile.H) + ((self.y / self.height) * Tile.V)

    def getTile(self):

        return Tile.getTile(self.getNumber())

    def rotate(self, direction, originalImg):

        if direction == 'n':
            if self.direction != 'n':
                self.direction = 'n'
                south = pygame.transform.rotate(originalImg, 90) # CCW
                self.img = pygame.transform.flip(south, False, True)

        if direction == 's':
            if self.direction != 's':
                self.direction = 's'
                self.img = pygame.transform.rotate(originalImg, 90) # CCW

        if direction == 'e':
            if self.direction != 'e':
                self.direction = 'e'
                self.img = pygame.transform.flip(originalImg, True, False)

        if direction == 'w':
            if self.direction != 'w':
                self.direction = 'w'
                self.img = originalImg

class Zombie(Character):

    List = []
    counter = 0 #counter
    d = (9,42,91,134,193,219,274)
    originalImg = pygame.image.load('images/zombie.png')
    health = 1000
    def __init__(self, x, y):

        self.direction = 'w'
        self.health = Zombie.health
        self.img = Zombie.originalImg
        Character.__init__(self, x, y)
        Zombie.List.append(self)
    @staticmethod
    def update(screen,survivor):
     #drawing zombies
    
        for zombie in Zombie.List:
            screen.blit(zombie.img, (zombie.x, zombie.y))
            if survivor.x % Tile.width == 0 and survivor.y % Tile.height == 0:
                 if zombie.x % Tile.width == 0 and zombie.y % Tile.height == 0:

                    tn  = survivor.getNumber()
                    N = tn + -(Tile.V)
                    S = tn + (Tile.V)
                    E = tn + (Tile.H)
                    W = tn + -(Tile.H)

                    NSEW = [N,S,E,W,tn]
                    if zombie.getNumber() in NSEW:
                        survivor.health -= 5        


            if zombie.health <= 0:
                Zombie.List.remove(zombie)
                Zombie.counter += 1 

     #movement of zombies 
            if zombie.tx != None and zombie.ty != None: # Target is set

                X = zombie.x - zombie.tx
                Y = zombie.y - zombie.ty

                vel = 4
                if X < 0: # --->
                    zombie.x += vel
                    zombie.rotate('e', Zombie.originalImg)

                elif X > 0: # <----
                    zombie.x -= vel
                    zombie.rotate('w', Zombie.originalImg)

                if Y > 0: # up
                    zombie.y -= vel
                    zombie.rotate('n', Zombie.originalImg)

                elif Y < 0: # dopwn
                    zombie.y += vel
                    zombie.rotate('s', Zombie.originalImg)

                if X == 0 and Y == 0:
                    zombie.tx, zombie.ty = None, None
 
    @staticmethod
    def spawn(totalFrames, FPS):
        if totalFrames % (FPS) == 0:
            if totalFrames % (FPS * 6) == 0:    
                r = randint(0,2)
                sound = [pygame.mixer.Sound('Audio/zs1.ogg'),
                        pygame.mixer.Sound('Audio/zs2.ogg'),
                        pygame.mixer.Sound('Audio/zs3.ogg')]
                sound = sound[ r ]
                sound.play()
            r = randint(0, len(Zombie.d) - 1)
            tile_num = Zombie.d[r]
            spawnNode = Tile.getTile(tile_num)
            Zombie(spawnNode.x, spawnNode.y)


class Survivor(Character):

    gunsImg = [pygame.image.load('images/pistol.png'),pygame.image.load('images/shotgun.png'),
                pygame.image.load('images/automatic.png')]
   
    def __init__(self, x, y):

        self.health = 1000
        self.current = 0 # 0 pistol ,1 shotgun, 2 automatic gun
        self.direction = 'w' 
        self.img = pygame.image.load('images/survivor_w.png')

        Character.__init__(self, x, y)


    def getBulletType(self):
        if self.current == 0:
            return 'pistol'
        elif self.current ==1:
            return 'shotgun'
        elif self.current == 2:
            return 'automatic'


    def movement(self):

        if self.tx != None and self.ty != None: # Target is set

            X = self.x - self.tx
            Y = self.y - self.ty

            vel = 8

            if X < 0: # --->
                self.x += vel
            elif X > 0: # <----
                self.x -= vel

            if Y > 0: # up
                self.y -= vel
            elif Y < 0: # dopwn
                self.y += vel

            if X == 0 and Y == 0:
                self.tx, self.ty = None, None

    def draw(self, screen):

        screen.blit(self.img, (self.x, self.y))

        h = self.width / 2
        img = Survivor.gunsImg[self.current]

        if self.direction == 'w':
            screen.blit(img, (self.x, self.y + h))

        elif self.direction == 'e':
            img = pygame.transform.flip(img, True, False)
            screen.blit(img, (self.x + h, self.y + h))            

        elif self.direction == 's':
            img = pygame.transform.rotate(img, 90) # CCW
            screen.blit(img, (self.x + h, self.y + h))            

        elif self.direction == 'n':
            south = pygame.transform.rotate(img, 90)
            img = pygame.transform.flip(south, False, True)
            screen.blit(img, (self.x + h, self.y - h))

    def rotate(self, direction):

        path = 'images/survivor_'
        png = '.png'

        if direction == 'n':
            if self.direction != 'n':
                self.direction = 'n'
                self.img = pygame.image.load(path + self.direction + png)

        if direction == 's':
            if self.direction != 's':
                self.direction = 's'
                self.img = pygame.image.load(path + self.direction + png)

        if direction == 'e':
            if self.direction != 'e':
                self.direction = 'e'
                self.img = pygame.image.load(path + self.direction + png)

        if direction == 'w':
            if self.direction != 'w':
                self.direction = 'w'
                self.img = pygame.image.load(path + self.direction + png)

class Bullet(pygame.Rect):
    count = 0
    width, height = 7,10
    List = []
    imgs = {'pistol':pygame.image.load('images/pistol_b.png'),
        'shotgun':pygame.image.load('images/shotgun_b.png'),
        'automatic':pygame.image.load('images/automatic_b.png'), }

    gunsDmg = {'pistol':(Zombie.health / 3) + 1,
               'shotgun':(Zombie.health / 2) ,
               'automatic':(Zombie.health / 6) + 1 }
    def   __init__(self, x,y,velx, vely,direction,type_):

        if type_ == 'shotgun' or type_ == 'pistol':
            try:
                dx = abs(Bullet.List[-1].x - x)
                dy = abs(Bullet.List[-1].y - y)
                if dx < 70 and dy <70 and type_ == 'shotgun':
                    return 
                if dx < 40 and dy < 40 and type_ == 'pistol':
                    return 
            except:
                pass
                

        self.type_ = type_
        self.direction = direction
        self.velx = velx
        self.vely = vely

        if direction == 'n':
            south = pygame.transform.rotate(Bullet.imgs[type_], 90) # CCW
            self.img = pygame.transform.flip(south, False, True)

        if direction == 's':
            self.img = pygame.transform.rotate(Bullet.imgs[type_], 90) # CCW

        if direction == 'e':
            self.img = pygame.transform.flip(Bullet.imgs[type_], True, False)

        if direction == 'w':

            self.img = Bullet.imgs[type_] 

        pygame.Rect.__init__(self,x,y,Bullet.width, Bullet.height)
        
        Bullet.List.append(self)

    #draw
    #update
    #collision
    def offScreen(self,screen):
        if self.x < 0:
            return True
        elif self.y <0 :
            return True
        elif self.x + self.width > screen.get_width():
            return True
        elif self.y + self.height > screen.get_height():
            return True
        return False

        
    @staticmethod
    def superMassiveJumbleLoop(screen):
        for bullet in Bullet.List:
            #looping through all the bullets

            bullet.x += bullet.velx
            bullet.y += bullet.vely
            #drawing all the bullets on the screen
            screen.blit(bullet.img,(bullet.x,bullet.y))
            #manybullets will be shooted, so just for convienience,
            if bullet.offScreen(screen) :
                Bullet.List.remove(bullet)
                continue
                #continue->for speed purpose

            for zombie in Zombie.List:

                if bullet.colliderect(zombie):
                    zombie.health -= Bullet.gunsDmg[bullet.type_]
                    Bullet.List.remove(bullet)
                    break   

            for tile in Tile.List:

                if bullet.colliderect(tile)and not(tile.walkable):
                    try:
                        Bullet.List.remove(bullet)
                    except :
                        pass #bullet not in the list





