import pygame
import os

#initialize pygame
pygame.init()

#create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("BLITTING IMAGES")

# Create images... returns a surface object with the image drawn on it
# we can than get the rect of the surface and use the rect to position the image
print(os.getcwd())
dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_left_rect.topright = (WINDOW_WIDTH, 0)


#the main game loop
running = True
while running:
    #loop through a list of Event objects that have occured
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Blit (copy) a surface object at the given 
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    pygame.draw.line(display_surface, (255, 255, 255), (0, 75), (WINDOW_WIDTH, 75), 4)

    pygame.display.update()

pygame.quit()