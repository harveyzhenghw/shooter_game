#import and int
import pygame, os
from bullet import Bullet
from grenade import Grenade
pygame.init()
max_accelaration_in_seconds = 0.3
GRAVITY = 0.5
JUMP_FORCE = 12

class Soldier(pygame.sprite.Sprite):
    def __init__(self,health, char_type, x_pos, y_pos, scale, speed, ammo):
        super().__init__()
        self.alive = True
        self.health = health
        self.max_helth = self.health#we need it for health bar for the future

        self.char_type = char_type

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.scale = scale
        
        
        self.speed = speed
        self.moving_right = False
        self.moving_left = False

        self.shoot_cooldown = 0
        self.shoot = False

        self.ammo = ammo
        self.start_ammo = self.ammo

        self.throwing_grenade = False

        self.flip = False
        self.direction = 1

        self.action = 0
        
        self.jump = False
        self.in_air = True



        self.velocity_y = 0

        self.current_speed = 0
        self.accel_step = self.speed / (100*max_accelaration_in_seconds)#60 == FPS



        

        self.animation_list = []
        self.frame_index = 0

        self.update_time = pygame.time.get_ticks()

        animation_types = ["Idle","Run",'Jump', "Death"]
        for animation in animation_types:



                
                temp_list = []
                #num_of frames in a folder
                num_of_frames = len(os.listdir(f"./assets/img/{self.char_type}/{animation}"))

                for i in range(num_of_frames):
                    original_img = pygame.image.load(f"./assets/img/{self.char_type}/{animation}/{i}.png")
                    img = pygame.transform.scale(
                    original_img,
                    (original_img.get_width()*scale, original_img.get_height()*scale)
                    ).convert_alpha()
                

                    temp_list.append(img)

                self.animation_list.append(temp_list)


        self.image = self.animation_list[self.action][self.frame_index]




        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)

        

    def update_animation(self):
        #update animation

        ANIMATION_COOLDOWN = 100
        #update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed
        if pygame.time.get_ticks()-self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index +=1
            if self.frame_index >= len(self.animation_list[self.action]):
               if self.action == 3:
                   self.frame_index = len(self.animation_list[self.action])-1
               else:
                   self.frame_index = 0

    def update_soldier(self):
        self.update_animation()
        #check if it the soldier_alive
        self.check_alive()


        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1



    def update_action(self, new_action):
        #check if the new action is different than the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()





    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def check_alive(self):
        if self.health <=0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)




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

        if self.jump and not self.in_air:
            self.velocity_y = -JUMP_FORCE
            self.jump = False
            self.in_air = True

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
        if self.velocity_y > JUMP_FORCE:
            self.velocity_y = JUMP_FORCE

        
        dx = self.current_speed
        dy = self.velocity_y

        #check collistion with floor

        if self.rect.bottom + dy > 500:
            dy = 500- self.rect.bottom
            self.in_air = False
        #update rect pos
        self.rect.x += int(dx)
        self.rect.y += int(dy)

    
    def shoot_a_bullet(self, screen_width, bullet_group):
        if self.shoot_cooldown == 0 and self.ammo>0:
            #At 100 FPS -> 20/60 = 0.33 seconds
            #The lower the number the faster you can shoot
            self.shoot_cooldown = 20
            self.ammo -= 1            

            bullet = Bullet(self.rect.centerx + (self.rect.size[0]*0.6*self.direction),self.rect.centery,self.direction,screen_width)
            self.shoot = False
            bullet_group.add(bullet)



    def throw_a_grenade(self,screen_width, grenade_group):
        grenade = Grenade(
            self.rect.centerx + (self.rect.size[0]*0.5*self.direction),
            self.rect.top,
            self.direction,
            screen_width

        )


        grenade_group.add(grenade)
        self.throwing_grenade = False
