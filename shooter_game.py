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
FPS = 60

#variables
game_is_running = True
background_color = (0,0,0)
#player
player_1 = Soldier(x_pos = 200, y_pos = 300, scale=2)


#game loop
while game_is_running:
    clock.tick(FPS)
    #fill background
    screen.fill(background_color)

        #display player img at player rect pos
    player_1.draw(screen)
    #game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False


    #update display
    pygame.display.update()
    

#quit pygame
pygame.quit()