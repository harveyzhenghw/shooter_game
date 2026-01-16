#import and int
import pygame
pygame.init()

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, scale, speed):
        super().__init__()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.scale = scale
        
        
        self.speed = speed
        self.moving_right = False
        self.moving_left = False



        original_img = pygame.image.load("./assets/img/player/Idle/0.png")
        self.image = pygame.transform.scale(
            original_img,
            (original_img.get_width()*scale, original_img.get_height()*scale)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    
