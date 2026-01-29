#import and int676
import pygame
pygame.init()


from soldier import Soldier
#screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 0.8 * SCREEN_WIDTH

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brave Hero")
#clock
clock = pygame.time.Clock()
FPS = 100

#variables
game_is_running = True
background_color = (0,0,0)
#player
player_1 = Soldier(char_type="player",x_pos = 200, y_pos = 300, scale=2, speed = 5)
enemy_1= Soldier(char_type="enemy",x_pos = 400, y_pos = 300, scale=2, speed = 5)


#game loop
while game_is_running:
    clock.tick(FPS)
    #fill background
    screen.fill(background_color)
    #moving player rect
    #PLAYER
    player_1.move()
    #display player img at player rect pos
    player_1.draw(screen)
    #ENEMY
    enemy_1.draw(screen)
  
    #game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

        

        

        #keyboard input(keydown)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player_1.moving_right = True
                pass
            if event.key == pygame.K_a:
                player_1.moving_left = True
                pass

        #keyboard input(keyup)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player_1.moving_right = False
                pass
            if event.key == pygame.K_a:
                player_1.moving_left = False
                pass





    #update display
    pygame.display.update()
    

#quit pygame
pygame.quit()