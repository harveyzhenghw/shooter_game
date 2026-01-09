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

#game loop
while game_is_running:
    clock.tick(FPS)
    #fill background
    screen.fill(background_color)

    #game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

    #update display
    pygame.display.update()

#quit pygame
pygame.quit()