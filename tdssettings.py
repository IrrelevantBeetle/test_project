import pygame, math, random, sys

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,  0, 255)


pygame.init()
clock = pygame.time.Clock()

class Enemy_var:
    def __init__ (self):
        self.cord = []
        self.health_current = []
        self.health_predict = []
        self.speed = []
        self.group = pygame.sprite.Group ()
tower_cord = []
tower_shoot = []
tower_distance = []
tower_type = []
total_guy = 0

screen_width, screen_hieght = 801, 801
class Main_var():
    def __init__ (self):
        self.screen = pygame.display.set_mode ((screen_width, screen_hieght)) 
        self.screen_width, self.screen_hieght = 801, 801
        self.game_time = 0
        self.person_choice = 'none'
    def Person_choice_set (self, new):
        self.person_choice = new
arrow_movement = 0
total = 0

mouseDownTime = 0
mouseDown = False
#person_choice = 'none'
money = 90000
font = pygame.font.Font(None,32)
player_health = 100
game_time = 0
game_time_change = 0

cost_text = font.render('     100          200          300          2000', True, WHITE)
cost_textRect = cost_text.get_rect()
cost_textRect.bottomleft = (0, 95)

  
start_text = font.render('Click Here', True, BLACK)
start_textRect = start_text.get_rect()
start_textRect.center = (screen_width/2, screen_hieght/2)

#pygame.mouse.set_visible(False)
curser_group = pygame.sprite.Group()
block_group = pygame.sprite.Group ()
path_group = pygame.sprite.Group ()
bullet_group = pygame.sprite.Group()
sword_group = pygame.sprite.Group()

    


