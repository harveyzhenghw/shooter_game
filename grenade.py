# import and init
import pygame
from explosion import Explosion
pygame.init()

GRAVITY = 0.6
TILE_SIZE = 100



class Grenade(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, direction, screen_width):
        super().__init__()

        # load grenade image
        self.image = pygame.image.load(
            f"./assets/img/icons/grenade.png"
        ).convert_alpha()

        # movement and liftime properties
        self.speed = 5
        self.vel_y = -10
        self.timer = 100

        # position and direction
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.direction = direction
        self.screen_width = screen_width

    def update(self, player, enemy_group, explosion_group):

        self.vel_y += GRAVITY

        dx = self.direction * self.speed
        dy = self.vel_y

        # check collision with fake floor
        if self.rect.bottom + dy > 500:
            dy = 500 - self.rect.bottom
            self.speed = 0

        # update grenade position
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.left + dx < 0 or self.rect.right + dx > self.screen_width:
            self.direction *= -1
            dx = self.direction * self.speed

        #counter timer

        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y, 1)
            explosion_group.add(explosion)


            #do damage to anyone near(no levels of nearness)

            ##do damage to player
            player = player.sprite
            if (abs(self.rect.centerx - player.rect.centerx)<TILE_SIZE * 2
                 and abs(self.rect.centery - player.rect.centery)<TILE_SIZE):
                player.health -= 50