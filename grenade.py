import pygame
pygame.init()







class Grenade(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos, direction, screen_width):
        super(). __init__()

        grenade_img = pygame.image.load(f"./assets/img/icons/grenade.png").convert_alpha()

        self.speed = 10
        self.image = grenade_img
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.direction = direction
        self.screen_width = screen_width