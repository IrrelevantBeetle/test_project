import pygame, math, random, sys
from tdssettings import *
enemy = Enemy_var ()
class Enemy (pygame.sprite.Sprite):
    def __init__ (self, posss, game_time):
        super().__init__()
        global money, player_health
        self.health = random.randint(2, 3 + game_time// 10000)
        #self.health = 3
        self.num = len (enemy.health_predict)
        enemy.health_predict.append(self.health)
        enemy.health_current.append(self.health)
        #self.num = posss
        self.image = pygame.Surface((13, 28), pygame.SRCALPHA)
        self.pfp = pygame.Surface((13, 28), pygame.SRCALPHA)
        
        #self.image.fill(WHITE)
        pygame.draw.ellipse(self.pfp, WHITE, [1,0,10,10], 0)
        pygame.draw.line(self.pfp, WHITE ,[5,17], [10,27], 2)
        pygame.draw.line(self.pfp, WHITE, [5,17], [0,27], 2)
        pygame.draw.line(self.pfp, RED, [5,17], [5,7], 2)
        pygame.draw.line(self.pfp, RED, [5,7], [9,17], 2)
        pygame.draw.line(self.pfp, RED, [5,7], [1,17], 2)
        self.image.blit(self.pfp, (0,5))
        self.rect = self.image.get_rect(center = (0, 400 + random.randint(0, 10000)/100))
        pos = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center = (pos[0], pos[1]))
        self.last_sword_hit = 0
        self.thing_x = 0
        self.speed = random.randint(4, 7)
        enemy.speed.append (self.speed)
        enemy.cord.append((self.rect.x,self.rect.y))
        
        if len(enemy.health_current) > len(enemy.health_predict):
            enemy.health_current.pop (len(enemy.health_current) - 1)
        if len(enemy.health_current) < len(enemy.health_predict):
            enemy.health_predict.pop (len(enemy.health_predict) - 1)
        
    def update (self):
        global debug, total_guy, money, player_health
        
        num = shiftingList (self.num)
        self.numy = self.num
        self.num -= num
        
        self.rect.x += self.speed
        self.image = pygame.Surface((20, 33), pygame.SRCALPHA)
        self.image.blit(self.pfp, (3,6))
        enemy.cord [self.num] = (self.rect.x, self.rect.y)
        health = enemy.health_current [self.num]
        
        if health > 0:
            
            color = 255/self.health * health
        if health <= 0:
            color = 0
        if color >= 255:
            color = 255
        pygame.draw.rect(self.image, (255-color, color, 0), [0, 0, 20/self.health*health, 5],0)
        pygame.draw.rect(self.image, (100, 100, 100), [0, 0, 20, 5],2)
        
        for k in range (1):
            if enemy.health_current [self.num] <= 0:
                
                #enemy.cord_shift.append (self.num)
                self.num = 0
                money += random.randint(30, 35)
                total_guy -= 1
                
                self.kill()
                
                
            if self.rect.x > screen_width - 10:
                
                player_health -= enemy.health_current [self.num]
                #enemy.cord_shift.append(self.num)
                enemy.health_predict [self.num] = 0
                enemy.health_current [self.num] = 0
                self.num = 0
                
                total_guy -= 1
                self.kill()
                
                
            if pygame.sprite.spritecollideany(self, sword_group) and abs(pygame.time.get_ticks() - self.last_sword_hit) > 800:
                self.last_sword_hit = pygame.time.get_ticks  ()
                enemy.health_current [self.num] -= 1
                enemy.health_predict [self.num] -= 1
