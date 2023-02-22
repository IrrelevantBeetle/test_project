import pygame, math, random, sys
from tdssettings import *
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,  0, 255)
enemy = Enemy_var ()
main = Main_var ()
class Path (pygame.sprite.Sprite):
    def __init__ (self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.main = Main_var ()
        self.image.fill ((0, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.arrow = pygame.Surface((100, 80), pygame.SRCALPHA)
        
        pygame.draw.line(self.image, GREEN ,[0,0], [0,100], 2)
        pygame.draw.line(self.image, GREEN ,[0,80], [80,100], 2)
        pygame.draw.line(self.arrow, WHITE, [15,50], [100,50], 2)
        pygame.draw.line(self.arrow, WHITE, [62.5,80], [100,50], 2)
        pygame.draw.line(self.arrow, WHITE, [62.5,20], [100,50], 2)
        self.image.blit(self.arrow, (0,0))

    def update (self, move):
        self.image.fill(BLACK)
        pygame.draw.line(self.image, GREEN ,[0,0], [100,0], 2)
        pygame.draw.line(self.image, GREEN ,[0,98], [100,98], 2)
        self.image.blit(self.arrow, (move,0))
        self.image.blit(self.arrow, (move - 100,0))
class Curser (pygame.sprite.Sprite):
    def __init__ (self, main):
        super().__init__()
        self.image = pygame.Surface((1000, 1000), pygame.SRCALPHA)
        self.main = main
        pygame.draw.rect(self.image, BLACK, [460,460,80,80], 10)
        pygame.draw.rect(self.image, GREEN, [460,460,80,80], 1)
        pos = pygame.mouse.get_pos ()
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))
    def update (self):
        pos = pygame.mouse.get_pos ()
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))
        if self.main.person_choice == 'none':
            
            self.image = pygame.Surface((1000, 1000), pygame.SRCALPHA)
        else:
            print ("debug")
        if self.main.person_choice == 'scout':
            pygame.draw.circle(self.image, (80, 80, 80, 125), (500, 500), 200, 0)
            #pygame.draw.rect(self.image, BLACK, [460,460,80,80], 10)
            pygame.draw.rect(self.image, GREEN, [460,460,80,80], 1)
            pygame.draw.circle(self.image, BLUE, (500, 500), 15, 0)
        if self.main.person_choice == 'gladiator':
            pygame.draw.circle(self.image, (80, 80, 80, 125), (500, 500), 100, 0)
            #pygame.draw.rect(self.image, BLACK, [460,460,80,80], 10)
            pygame.draw.rect(self.image, GREEN, [460,460,80,80], 1)
            pygame.draw.circle(self.image, WHITE, (500, 500), 15, 0)
            
        
        if self.main.person_choice == 'solider':
            
            pygame.draw.circle(self.image, (80, 80, 80, 125), (500, 500), 350, 0)
            #pygame.draw.rect(self.image, BLACK, [460,460,80,80], 10)
            pygame.draw.rect(self.image, GREEN, [460,460,80,80], 1)
            pygame.draw.circle(self.image, GREEN, (500, 500), 15, 0)
        if self.main.person_choice == 'minigun':
            
            pygame.draw.circle(self.image, (80, 80, 80, 125), (500, 500), 500, 0)
            #pygame.draw.rect(self.image, BLACK, [460,460,80,80], 10)
            pygame.draw.rect(self.image, GREEN, [460,460,80,80], 1)
            pygame.draw.circle(self.image, RED, (500, 500), 15, 0)
        main.screen.blit(self.image, pos)
            
        
def person_selection (main, person):
    global money
    if main.person_choice == 'scout':        
        pygame.draw.rect(main.screen, GREEN, [10,10,80,80], 1)
    elif main.person_choice == 'gladiator':
        pygame.draw.rect(main.screen, GREEN, [110,10,80,80], 1)
    elif main.person_choice == 'solider':        
        pygame.draw.rect(main.screen, GREEN, [210,10,80,80], 1)
    elif main.person_choice == 'minigun':        
        pygame.draw.rect(main.screen, GREEN, [310,10,80,80], 1)
    if pygame.mouse.get_pressed()[0] == False:
        #*main.person_choice = 'none'
        pass
    if pygame.mouse.get_pressed()[0] == True:
        pos = pygame.mouse.get_pos ()
        for x in range (1):
            if pos [1] > 100:
                continue
            if pos [0] < 100:
                main.Person_choice_set ('scout')
            elif pos [0] < 200:
                main.Person_choice_set ('gladiator')
                
            elif pos [0] < 300:
                main.Person_choice_set ('solider')
            elif pos [0] < 400:
                main.Person_choice_set ('minigun')
        
            
    pygame.draw.circle(main.screen, BLUE, (50, 50), 15, 0)
    pygame.draw.circle(main.screen, WHITE, (150, 50), 15, 0)
    
    pygame.draw.circle(main.screen, GREEN, (250, 50), 15, 0)
    pygame.draw.circle(main.screen, RED, (350, 50), 15, 0)
    return person
def shooting ():
    global bullet_group
    if len(enemy.cord) > 30:
        
        #num = random.randint(len(enemy.cord) - total_guy + 30, len(enemy.cord))
        num = random.randint(len(enemy.cord) - 30, len(enemy.cord))
    else:
        num = 0
    for x in range (num, len(enemy.cord)):
        if enemy.health_predict [x] <= 0:
            continue
        
        for y in range (len(tower_cord)):
            if tower_shoot [y] == False:
                continue
            numx, numy = enemy.cord [x] [0], enemy.cord [x] [1]
            numx = numx + 6 - tower_cord [y] [0] - 50
            numy = numy + 14 - tower_cord[y] [1] - 50
            
            if math.sqrt(numx ** 2 + numy ** 2) > tower_distance [y] + 50:
                continue
            tower_shoot [y] = False
            
            if tower_type [y] == 'gladiator':
                sword = Sword (tower_cord [y] [0] + 50, tower_cord[y] [1] + 50, numx + 6, numy + 14, x, y)
                sword_group.add (sword)
                
                continue
            if enemy.health_predict [x] <= 0:
                continue
            
            enemy.health_predict [x] -= 1
            bullet = Bullet (tower_cord [y] [0] + 50, tower_cord[y] [1] + 50, numx + 6, numy + 14, x, y)
            bullet_group.add(bullet)
            
    for x in range (0, num):
         if enemy.health_predict [x] <= 0:
            continue
        
         for y in range (len(tower_cord)):
            if tower_shoot [y] == False:
                continue
            numx, numy = enemy.cord [x] [0], enemy.cord [x] [1]
            numx = numx + 6 - tower_cord [y] [0] - 50
            numy = numy + 14 - tower_cord[y] [1] - 50
            
            if math.sqrt(numx ** 2 + numy ** 2) > tower_distance [y] + 50:
                continue
            enemy.health_predict [x] -= 1
            tower_shoot [y] = False
            
            if tower_type [y] == 'gladiator':
                sword = Sword (tower_cord [y] [0] + 50, tower_cord[y] [1] + 50, numx + 6, numy + 14, x, y)
                sword_group.add (sword)
                
                continue
            if enemy.health_predict [x] <= 0:
                continue
            
            bullet = Bullet (tower_cord [y] [0] + 50, tower_cord[y] [1] + 50, numx + 6, numy + 14, x, y)
            bullet_group.add(bullet)
        
            
            
def shiftingList (num):
    total = 0
    for x in range (0, len(enemy.cord_shift)):
        if enemy.cord_shift[x] < num:
            total += 1
    
    
    '''
    if total >= 0:
        total = 0
    total = len (enemy.cord_shift)
    #total = len (enemy.cord_shift)
    '''
    
    return total


