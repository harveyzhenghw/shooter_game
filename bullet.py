import pygame
pygame.init()







class Bullet(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos, direction):
        super(). __init__()

        bullet_img = pygame.image.load(f"./assets/img/icons/bullet.png").convert_alpha()

        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.direction = direction