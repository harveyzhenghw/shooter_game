import pygame
pygame.init()







class Bullet(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos, direction, screen_width):
        super(). __init__()

        bullet_img = pygame.image.load(f"./assets/img/icons/bullet.png").convert_alpha()

        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.direction = direction
        self.screen_width = screen_width

    def update(self,player,enemy_group):
        #move bullet
        self.rect.x += self.speed* self.direction
        #check if bullet is off screen
        if self.rect.right < 0 or self.rect.left > self.screen_width:
            self.kill()

        
            if pygame.sprite.spritecollide(self,player,False):
                
                    if player.alive:
                        player_health -= 10
                        #delete bullet
                        self.kill
                        
                        return








        #hit ANY enemy

        hits = pygame.sprite.spritecollide(self,enemy_group, False)
        if hits:
            for enemy in hits:
                if enemy.alive:
                    #bullet_hit_logic
                    enemy.health-=25
                    #delete bullet
                    self.kill()
                    return