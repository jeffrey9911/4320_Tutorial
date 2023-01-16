import pygame

#initialize pygame
pygame.init()

#create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Text")

GREEN = (0, 255, 0)
DARKGREEN = (15, 50, 10)


# see all available system fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)


# define fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('CusFont.ttf', 32)

# define text
system_text = system_font.render("Dragons Rule!", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_text = custom_font.render("Move the dragon soon!", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

#the main game loop
running = True
while running:
    #loop through a list of Event objects that have occured
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)
    pygame.display.update()

pygame.quit()