import pygame, sys

print "Loading..."

background = pygame.image.load("C:/Users\Miller/Desktop/Python RPG repo/A-Python-RPG/Sprites/title/background.png")
title = pygame.image.load("C:/Users\Miller/Desktop/Python RPG repo/A-Python-RPG/Sprites/title/title.png")
print "Loaded ALL the things!"

screen = pygame.display.set_mode([744, 744])

screen.blit(background, [0, 0])
screen.blit(title, [135, 47])
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()