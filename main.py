print "Loading..."

import pygame, sys

folder = open('folder.txt', 'r')
folderinfo = folder.readline()

background = pygame.image.load(folderinfo + "/Sprites/title/background.png")
title = pygame.image.load(folderinfo + "/Sprites/title/title.png")

print "Loaded ALL the things!"

screen = pygame.display.set_mode([744, 744])

screen.blit(background, [0, 0])
screen.blit(title, [135, 47])
pygame.display.flip()
folder.close
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()