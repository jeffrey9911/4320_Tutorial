import pygame
import os

#initialize pygame
pygame.init()

#create a display surface and set its caption
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("DISCRETE KEYBOARD MOVEMENT")



dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.centerx = WINDOW_WIDTH//2
dragon_left_rect.bottom = WINDOW_HEIGHT

VELOCITY = 1

#the main game loop
running = True
while running:
    #loop through a list of Event objects that have occured
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # delta time
    

    # check for discrete movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            dragon_left_rect.y -= VELOCITY

        if event.key == pygame.K_LEFT:
            dragon_left_rect.x -= VELOCITY

        if event.key == pygame.K_DOWN:
            dragon_left_rect.y += VELOCITY

        if event.key == pygame.K_RIGHT:
            dragon_left_rect.x += VELOCITY

    display_surface.fill((0, 0, 0))
    display_surface.blit(dragon_left_image, dragon_left_rect)
    pygame.display.update()

pygame.quit()