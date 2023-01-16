import pygame

#initialize pygame
pygame.init()

#create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sounds")

# load sound effects
sound_1 = pygame.mixer.Sound('sound1.mp3')
sound_2 = pygame.mixer.Sound('sound2.mp3')

# Play the sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

# change the volume of a sound effect
sound_2.set_volume(.1)
sound_2.play()

# load background music
pygame.mixer_music.load('sound2.mp3')

# play and stop the music
pygame.mixer_music.play(-1, 0.0)
pygame.time.delay(5000)
pygame.mixer_music.stop()

#the main game loop
running = True
while running:
    #loop through a list of Event objects that have occured
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()