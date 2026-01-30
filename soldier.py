#import and int
import pygame
pygame.init()
max_accelaration_in_seconds = 0.35
GRAVITY = 0.5

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x_pos, y_pos, scale, speed):
        super().__init__()

        self.char_type = char_type

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.scale = scale
        
        
        self.speed = speed
        self.moving_right = False
        self.moving_left = False

        self.flip = False
        self.direction = 1
        
        self.jump = False
        self.velocity_y = 0

        self.current_speed = 0
        self.accel_step = self.speed / (100*max_accelaration_in_seconds)#60 == FPS



        original_img = pygame.image.load(f"./assets/img/{self.char_type}/Idle/0.png")
        self.image = pygame.transform.scale(
            original_img,
            (original_img.get_width()*scale, original_img.get_height()*scale)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
    def move(self):
        #reset movment
        dx = 0
        dy = 0

        target_speed = 0

        #right
        if self.moving_right:
            target_speed = self.speed
            self.flip = False
            self.direction = 1
            pass
        #left
        if self.moving_left:
            target_speed = -self.speed
            self.flip = True
            self.direction = -1
            pass

        if self.jump:
            self.velocity_y = -10
            self.jump = False

        #gradually move the current_speed toward the target_speed
        if self.current_speed < target_speed:
            self.current_speed += self.accel_step
            if self.current_speed > target_speed:
                self.current_speed = target_speed
        elif self.current_speed > target_speed:
            self.current_speed -= self.accel_step
            if self.current_speed < target_speed:
                self.current_speed = target_speed


        #apply gravity
        self.velocity_y += GRAVITY
        if self.velocity_y > 10:
            self.velocity_y = 10

        
        dx = self.current_speed
        dy = self.velocity_y

        #check collistion with floor

        if self.rect.bottom + dy > 500:
            dy = 500- self.rect.bottom
        #update rect pos
        self.rect.x += int(dx)
        self.rect.y += int(dy)

    
