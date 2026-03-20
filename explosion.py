# import and init
import pygame, os

pygame.init()

GRAVITY = 0.6


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, scale):
        super().__init__()

        #load explosion images

        self.images = []
        num_of_frames = len(os.listdir(f"./assets/img/explosion"))

        

        for i in range(num_of_frames):
            img = pygame.image.load(
             f"./assets/img/explosion/exp{i+1}.png"
             ).convert_alpha()
            

            img = pygame.transform.scale(img, (int(img.get_width()*scale),int(img.get_height()*scale)))
            self.images.append(img)
            


        # movement and liftime properties

       
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)

        self.counter = 0
        

   