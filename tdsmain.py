import pygame, math, random, sys
from tdssettings import *
from tdsfunctionspersonchoice import *
from tdstower import *
from tdsbullet import *
from tdsenemy import *
from tdspath import *
game_time = 0
enemy = Enemy_var ()
main = Main_var ()
enemys = Enemy(len(enemy.cord), game_time)
enemy.group.add(enemys)
total_guy += 1

curser = Curser (main)
curser_group.add (curser)
for x in range (50, main.screen_width, 100):
    path = Path (x, 450)
    path_group.add (path)
    


    
    
    

class GameState ():
    def __init__ (self):
        self.state = 'menu'

    def Game (self):
        global mouseDown, bullet_group, arrow_movement, total_guy, game_time
        enemy = Enemy_var ()
        game_time = pygame.time.get_ticks () - game_time_change
        enemy.cord_shift = []
        if mouseDown == True:
            mouseDown = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
                mouseDownTime = game_time
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    enemy = Enemy(len(enemy.cord))
                    enemy.group.add(enemy)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos ()
                block = Block (pos[0], pos[1])
                block_group.add (block)
                main.person_choice = 'none'
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for x in range (1):
                        enemy = Enemy(len(enemy.cord))
                        enemy.group.add(enemy)
        if game_time % 4000 < 17 + game_time ** 2 // 90000000:
            for x in range (0):
                enemy = Enemy(len(enemy.cord))
                enemy.group.add(enemy)
                total_guy += 1
        
        block_group.update()
                        
        #drawing
        arrow_movement += 2
        if arrow_movement > 100:
            arrow_movement -= 100
        main.screen.fill((0, 0, 0))
        person_selection(main, main.person_choice)
        block_group.update()
        shooting()
        bullet_group.update()
        path_group.update(arrow_movement)
        enemy.group.update()
        curser_group.update()
        sword_group.update()
        block_group.draw (main.screen)
        path_group.draw (main.screen)
        enemy.group.draw (main.screen)
        bullet_group.draw (main.screen)
        curser_group.draw (main.screen)
        sword_group.draw (main.screen)
        
        money_text = font.render('Money = ' + str(money), True, WHITE)
        money_textRect = money_text.get_rect()
        money_textRect.topright = (main.screen_width, 8)
        health_text = font.render('Health = ' + str(player_health), True, WHITE)
        health_textRect = health_text.get_rect()
        health_textRect.topright = (main.screen_width, money_textRect.h + 8)
        
        main.screen.blit(money_text, money_textRect)
        main.screen.blit(health_text, health_textRect)
        
        t = font.render(f'choice = {main.person_choice}, {pygame.mouse.get_pos()}', True, WHITE)
        tr = health_text.get_rect()
        tr.topright = (main.screen_width - 500, money_textRect.h + 40)
        main.screen.blit(t, tr)

        main.screen.blit(cost_text, cost_textRect)
        if player_health <= 0:
            main.screen.fill (WHITE)
            self.state = 'menu'
    def Menu (self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if abs(pos[0] - main.screen_width/2) < start_textRect.w:
                    if abs(pos[1] - main.screen_hieght/2) < start_textRect.h:
                        self.state = 'restart'
                
                
        main.screen.fill (WHITE)
        main.screen.blit(start_text, start_textRect)
    def Restart (self):
        global block_group, player_health, money, bullet_group
        global game_time_change, tower_cord, tower_shoot, tower_distance, total_guy
        enemy.cord = []
        enemy.health_current = []
        enemy.health_predict = []
        enemy.speed = []
        tower_cord = []
        tower_shoot = []
        tower_distance = []
        total_guy = 0
        game_time_change = pygame.time.get_ticks()
        player_health = 100
        money = 40000
        enemy.group = pygame.sprite.Group ()
        block_group = pygame.sprite.Group ()
        bullet_group = pygame.sprite.Group ()
        
        self.state = 'game'
        
    def state_manger (self):
        while True:
            if self.state == 'game':
                self.Game ()
            if self.state == 'menu':
                self.Menu ()
            if self.state == 'restart':
                self.Restart ()
            pygame.display.flip()
            clock.tick(30)








game_state = GameState ()

if __name__ == '__main__':
    game_state.state_manger ()
    print(self.setting.person_choice)
    