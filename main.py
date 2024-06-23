import pygame

#Initialize pygame
pygame.init()

#Create display window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Feed the Dragon')



#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



#Quit game
pygame.quit()
