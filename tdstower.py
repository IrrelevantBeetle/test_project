import pygame, math, random, sys
from tdssettings import *

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,  0, 255)


enemy = Enemy_var ()
main = Main_var ()
class Block (pygame.sprite.Sprite):
    def __init__ (self, x, y):
        super().__init__()
        #global enemy.health_predict, tower_cord, money, self.main.game_time
        self.main = Main_var()
        main = Main_var ()
        print (self.main.person_choice)
        self.image = pygame.Surface((80, 80), pygame.SRCALPHA)
        self.image.fill ((255, 255, 255))
        pygame.draw.rect(self.image, BLACK, [0,0,80,80], 10)
        pygame.draw.rect(self.image, GREEN, [0,0,80,80], 1)
        self.rect = self.image.get_rect(center=(x, y))
        self.state = 'none'
        self.last_shot = self.main.game_time
        self.speed = 9999999999999999999999999
        self.death = False
        if self.rect.y < 80:
            self.death = True
        for pos in tower_cord:
            if abs(pos [0] - self.rect.x) > 80:
                continue
            if abs(pos [1] - self.rect.y) > 80:
                continue
            self.death = True
        if self.rect.x < 5:
            self.death = True
        if self.rect.y < 5:
            self.death = True
        if self.rect.x > screen_width - 80:
            self.death = True
        if self.rect.y > screen_hieght - 80:
            self.death = True
        
        '''
        if pygame.sprite.spritecollideany(self, path_group):
            self.death = True
        '''
        if abs (self.rect.y + 40 - 450) < 80:
            self.death = True
        self.num = len(tower_cord)
        tower_cord.append ((self.rect.x, self.rect.y))
        tower_shoot.append (False)
        tower_distance.append (0)
        tower_type.append ('none')
        for x in range (1):
            
            if self.main.person_choice == 'none':
                self.death = True
                #print ('choice is none')
                continue
            if self.death == True:
                continue
            
            
            if self.main.person_choice == 'scout':
                if money < 100:
                    self.death = True
                    continue
                money -= 100
                
                self.image.fill ((0,0,0))
                pygame.draw.circle(self.image, BLUE, (40, 40), 15, 0)
                tower_distance [self.num] = 250
                self.state = 'scout'
                self.speed = 800
            if self.main.person_choice == 'gladiator':
                if money < 200:
                    self.death = True
                    continue
                money -= 200
                
                self.image.fill ((0,0,0))
                pygame.draw.circle(self.image, WHITE, (40, 40), 15, 0)
                tower_distance [self.num] = 150
                self.state = 'gladiator'
                self.speed = 800
            
            if self.main.person_choice == 'solider':
                if money < 300:
                    self.death = True
                    continue
                money -= 300
                tower_distance [self.num] = 350
                self.speed = 200
                self.image.fill ((0,0,0))
                pygame.draw.circle(self.image, GREEN, (40, 40), 15, 0)
                self.state = 'solider'
            if self.main.person_choice == 'minigun':
                if money < 2000:
                    self.death = True
                    continue
                money -= 2000
                tower_distance [self.num] = 550
                self.speed = 50
                self.image.fill ((0,0,0))
                pygame. draw. circle(self.image, RED, (40, 40), 15, 0)
                self.state = 'minigun'
        pygame.draw.rect(self.image, GREEN, [0,0,80,80], 1)
        tower_type [self.num] = self.state
    def update (self):
        global total, money, bullet_group
        pos = pygame.mouse.get_pos()
        
            
        for k in range (1):
            if len (tower_shoot) <= self.num:
                continue
            tower_shoot [self.num] = False
            
            if self.main.game_time - self.last_shot > 10 and self.main.game_time - self.last_shot < self.speed:
                break
            
            if self.state == 'none':
                break
            
            tower_shoot [self.num] = True
            self.last_shot = self.main.game_time
        if abs(pos [0] - self.rect.x) < 100 and abs(pos [1] - self.rect.y) < 100 and mouseDown == True:
            self.death = True
            
        
        if self.death == True:
            
            tower_shoot [self.num] = False
            self.death = False
            self.kill()
            
class Sword (pygame.sprite.Sprite):
    def __init__ (self, x, y, x_velocity, y_velocity, target_num, tower_num):
        super().__init__()
        self.sword = pygame.Surface ((100, 10), pygame.SRCALPHA)
        self.sword.fill (GREEN)
        self.sword2 = pygame.Surface ((200, 10), pygame.SRCALPHA)
        self.sword2.blit (self.sword, (100, 0))
        self.image = self.sword2
        self.rect = self.image.get_rect(center = (x, y))
        self.x = x
        self.y = y
        self.angle = 0
    def update (self):
        if self.y > 450:
            self.image = pygame.transform.rotozoom(self.sword2, self.angle, 1)
        else:
            self.image = pygame.transform.rotozoom(self.sword2, (self.angle * -1) + 360, 1)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.angle += 14
        if self.angle >= 180:
            self.kill ()
            