#import and int676
import pygame
pygame.init()
#screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 0.8 * SCREEN_WIDTH

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brave Hero")
#clock
clock = pygame.time.Clock()
FPS = 60

#variables
game_is_running = True
background_color = (0,0,0)
#player
player_x_pos = 200
player_y_pos = 200
player_scale = 2
player_img = pygame.image.load("./assets/img/player/idle/0.png")
player_img = pygame.transform.scale(player_img,(player_img.get_width()*player_scale, player_img.get_height()*player_scale) )
player_rect = player_img.get_rect()
player_rect.center = (player_x_pos, player_y_pos)

#game loop
while game_is_running:
    clock.tick(FPS)
    #fill background
    screen.fill(background_color)
    #display player img at player rect pos
    screen.blit(player_img, player_rect)

    #game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

    #update display
    pygame.display.update()

#quit pygame
pygame.quit()