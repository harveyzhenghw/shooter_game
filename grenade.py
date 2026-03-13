import pygame
pygame.init()
GRAVITY = 0.5






class Grenade(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos, direction, screen_width):
        super(). __init__()

        self.image = pygame.image.load(f"./assets/img/icons/grenade.png").convert_alpha()

        #movement and lifetime properties
        self.vel_y = -10
        self.timer = 100
        self.speed = 5
        #position and direction
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.direction = direction
        self.screen_width = screen_width


    def update(self,player,enemy_group):
        
        self.vel_y += GRAVITY

        dx = self.direction*self.speed
        dy = self.vel_y

        #check collision with fake floor
        if self.rect.bottom + dy > 500:
            dy = 500-self.rect.bottom
            self.speed = 0
            


        #update grenade position

        self.rect.x += dx
        self.rect.y += dy