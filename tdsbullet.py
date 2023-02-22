import pygame, math, random, sys
class Bullet (pygame.sprite.Sprite):
    def __init__(self, x, y, x_velocity, y_velocity, target_num, tower_num):
        super().__init__ ()
        global enemy_health_predict, money
        self.tower_num = tower_num
        self.target = target_num
        num = math.sqrt(x_velocity ** 2 + y_velocity ** 2)
        x_velocity += num/20 * enemy_speed [self.target]
        self.new_x = x_velocity
        self.new_y = y_velocity
        #num = 5 / num
        num = num / 20
        
        self.velocity_x = x_velocity / num
        self.velocity_y = y_velocity / num
        
        self.bullet = pygame.image.load("images.png")
        angle = math.degrees(math.atan(self.velocity_y * -1 / self.velocity_x))
        if self.velocity_x < 0:
            angle += 180
        self.image = pygame.transform.rotozoom(self.bullet, angle, 0.0925)
        self.rect = self.image.get_rect(center = (x, y))
        self.hit = False
    def update (self):
        global enemy_health_current
        num = shiftingList (self.target)
        self.target -= num
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        if self.rect.x < -100 or self.rect.y < -100 or self.rect.x > screen_width + 100 or  self.rect.y > screen_hieght+ 100:
            if len (enemy_cord) > self.target:
                enemy_health_current [self.target] -= 1
                
            self.kill ()
        if len (enemy_cord) < self.target:
            self.kill()
        if abs(self.rect.x - self.new_x - 6) > 20 and abs(self.rect.y - self.new_y - 14) > 20:
            self.hit = True
        for x in range (1):
            if len (enemy_cord) <= self.target:
                break
            if abs(self.rect.x - enemy_cord[self.target][0] - 6) > 50:
                break
            if abs(self.rect.y - enemy_cord[self.target][1] - 14) > 50:
                break
            if enemy_health_current [self.target] < enemy_health_predict [self.target]:
                break
            if enemy_health_current [self.target] <= 0:
                break
            enemy_health_current [self.target] -= 1
            self.kill()
