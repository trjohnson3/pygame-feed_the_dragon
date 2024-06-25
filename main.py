import pygame, random

#Initialize pygame
pygame.init()

#Create display window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Feed the Dragon')

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
PLAYER_STARTING_LIVES = 5
VELOCITY = 5
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

#Set colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Set fonts
font = pygame.font.Font('./fonts/AttackGraffiti.ttf', 32)

#Set text
score_text = font.render("Score: " + str(score), True, GREEN, BLACK)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Feed the Dragon", True, GREEN, BLACK)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10


lives_text = font.render("Lives: " + str(player_lives), True, GREEN, BLACK)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAMEOVER", True, GREEN, BLACK)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to continue", True, GREEN, BLACK)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

#Set sounds and music
coin_sound = pygame.mixer.Sound('./sounds/coin.wav')
miss_sound = pygame.mixer.Sound('./sounds/miss.wav')
# miss_sound.set_volume(.1)
pygame.mixer.music.load("./sounds/background.wav")

#Set images
player_image = pygame.image.load('./images/dragon_right.png')
player_rect = player_image.get_rect()
player_rect.x = 32
player_rect.centery = WINDOW_HEIGHT//2

coin_image = pygame.image.load('./images/coin.png')
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 48)




#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Filling display
    display.fill(BLACK)

    #Blit the hud
    display.blit(score_text, score_rect)
    display.blit(lives_text, lives_rect)
    display.blit(title_text, title_rect)
    pygame.draw.line(display, WHITE, (0, 64), (WINDOW_WIDTH, 64), 2)

    #Blit images
    display.blit(player_image, player_rect)
    display.blit(coin_image, coin_rect)
    

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#Quit game
pygame.quit()
