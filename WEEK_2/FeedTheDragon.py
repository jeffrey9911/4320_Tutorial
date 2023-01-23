import pygame
import random

# initialize pygame
pygame.init()

# create a display surface and set its caption
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

def resetCoin():
    rect_coin.x = WINDOW_WIDTH + BUFFER_DISTANCE
    rect_coin.y = random.randint(64, WINDOW_HEIGHT - 32)

# Assets load
# FPS & CLOCK
FPS = 120
clock = pygame.time.Clock()

# Game Values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY
level = 0

txt_color_timer = 0.0

# Set Colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
back_color_random = (0, 0, 0)

deltaTime = clock.tick(FPS) / 1000

# Set fonts
custom_font_60 = pygame.font.Font('CusFont.ttf', 60)
custom_font_30 = pygame.font.Font('CusFont.ttf', 30)

# Set sounds
snd_goal = pygame.mixer.Sound("goal.mp4")
snd_loss = pygame.mixer.Sound("loss.mp4")
#snd_loss.set_volume(.1)
pygame.mixer.music.load("bgm.mp4")

# Set Images
img_player = pygame.image.load("dragon.png")
rect_player = img_player.get_rect()
rect_player.left = 32
rect_player.centery = WINDOW_HEIGHT//2

img_coin = pygame.image.load("coin.png")
rect_coin = img_coin.get_rect()
rect_coin.x = WINDOW_WIDTH + BUFFER_DISTANCE
rect_coin.y = random.randint(64, WINDOW_HEIGHT - 32)

# Set Texts
txt_title = custom_font_60.render("FEED THE DRAGON", True, (200, 30, 30))
txt_title_rect = txt_title.get_rect()
txt_title_rect.center = (WINDOW_WIDTH//2, 40)

txt_score = custom_font_30.render("Score: " + str(score), True, WHITE)
txt_score_rect = txt_score.get_rect()
txt_score_rect.topleft = (40, 40)

txt_lives = custom_font_30.render("HP: " + str(player_lives), True, WHITE)
txt_lives_rect = txt_lives.get_rect()
txt_lives_rect.topright  = (WINDOW_WIDTH - 40, 40)

txt_gameover = custom_font_60.render("GAME IS OVER", True, (255, 0, 0))
txt_gameover_rect = txt_gameover.get_rect()
txt_gameover_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

txt_continue = custom_font_30.render("Press Any Key To Play Again", True, GREEN, DARKGREEN)
txt_continue_rect = txt_continue.get_rect()
txt_continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50)

pygame.mixer.music.play(-1, 0.0)

# the main game loop
running = True
while running:
    # loop through a list of Event objects that have occurred
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if(txt_color_timer >= 2):
        txt_title = custom_font_60.render("FEED THE DRAGON", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        back_color_random = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        txt_color_timer -= 2.0
    
    txt_color_timer += deltaTime

    # keyboard movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and rect_player.top > 80:
        rect_player.y -= PLAYER_VELOCITY

    if keys[pygame.K_s] and rect_player.bottom < WINDOW_HEIGHT:
        rect_player.y += PLAYER_VELOCITY
    
    if(rect_player.colliderect(rect_coin)):
        score += 1
        coin_velocity += COIN_ACCELERATION
        snd_goal.play()
        resetCoin()
        

    if(rect_coin.right <= 0):
        player_lives -= 1
        snd_loss.play()
        resetCoin()

    txt_lives = custom_font_30.render("HP: " + str(player_lives), True, WHITE)
    txt_score = custom_font_30.render("Score: " + str(score), True, WHITE)

    # draw
    display_surface.fill(back_color_random)

    if player_lives == 0:
        display_surface.blit(txt_gameover, txt_gameover_rect)
        display_surface.blit(txt_continue, txt_continue_rect)
        pygame.mixer.music.stop()
        pygame.display.update()
        pause = True
        while pause:
            for event in pygame.event.get():
                
                if(event.type == pygame.KEYDOWN):
                    resetCoin()
                    player_lives = 5
                    score = 0
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    pause = False
                    break

                if event.type == pygame.QUIT:
                    pause = False
                    running = False
                    break

    rect_coin.x -= coin_velocity 

    display_surface.blit(txt_title, txt_title_rect)
    display_surface.blit(txt_score, txt_score_rect)
    display_surface.blit(txt_lives, txt_lives_rect)

    pygame.draw.line(display_surface, WHITE, (0,80), (WINDOW_WIDTH, 80), 2)

    display_surface.blit(img_coin, rect_coin)
    display_surface.blit(img_player, rect_player)
    
    

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()



