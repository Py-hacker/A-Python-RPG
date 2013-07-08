print "Loading..."

import pygame, sys

folder = open('folder.txt', 'r')
folderinfo = folder.readline()

background = pygame.image.load(folderinfo + "/Sprites/title/background.png")
title = pygame.image.load(folderinfo + "/Sprites/title/title.png")
play_button = pygame.image.load(folderinfo + "/Sprites/title/interface/play_button.png")
options_button = pygame.image.load(folderinfo + "/Sprites/title/interface/options_button.png")
button_overlay_1 = pygame.image.load(folderinfo + "/Sprites/title/interface/overlay_1.png")
save1 = pygame.image.load(folderinfo + "/Sprites/title/interface/saves/Save_1.png")
save2 = pygame.image.load(folderinfo + "/Sprites/title/interface/saves/Save_2.png")
save3 = pygame.image.load(folderinfo + "/Sprites/title/interface/saves/Save_3.png")
print "Loaded ALL the things!"

screen = pygame.display.set_mode([744, 744])

screen.blit(background, [0, 0])
screen.blit(title, [135, 47])
screen.blit(play_button, [253, 300])
screen.blit(options_button, [253, 441])
screen.blit(button_overlay_1, [243, 290])
overlay_pos = 0
pygame.display.flip()
folder.close
while True:
    screen.blit(background, [0, 0])
    screen.blit(title, [135, 47])
    screen.blit(play_button, [253, 300])
    screen.blit(options_button, [253, 441])
    screen.blit(button_overlay_1, [243, 290])
    overlay_pos = 0
    pygame.display.flip()
    stay1 = True
    while stay1 == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if overlay_pos == 0:
                        screen.blit(background, [0, 0])
                        screen.blit(title, [135, 47])
                        screen.blit(play_button, [253, 300])
                        screen.blit(options_button, [253, 441])
                        screen.blit(button_overlay_1, [243, 431])
                        pygame.display.flip()
                        overlay_pos = 1
                    else:
                        pass
                elif event.key == pygame.K_UP:
                    if overlay_pos == 1:
                        screen.blit(background, [0, 0])
                        screen.blit(title, [135, 47])
                        screen.blit(play_button, [253, 300])
                        screen.blit(options_button, [253, 441])
                        screen.blit(button_overlay_1, [243, 290])
                        pygame.display.flip()
                        overlay_pos = 0
                    else:
                        pass
                elif event.key == pygame.K_RETURN:
                    if overlay_pos == 0:
                        screen.blit(background, [0, 0])
                        screen.blit(save1, [93, 30])
                        screen.blit(save2, [93, 278])
                        screen.blit(save3, [93, 526])
                        screen.blit(button_overlay_1,[83, 20])
                        overlay_pos2 = 0 
                        pygame.display.flip()
                        stay2 = True
                        while stay2 == True:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_DOWN:
                                        if overlay_pos2 == 0:
                                            screen.blit(background, [0, 0])
                                            screen.blit(save1, [93, 30])
                                            screen.blit(save2, [93, 278])
                                            screen.blit(save3, [93, 526])
                                            screen.blit(button_overlay_1,[83, 268])
                                            overlay_pos2 = 1
                                            pygame.display.flip()
                                        elif overlay_pos2 == 1:
                                            screen.blit(background, [0, 0])
                                            screen.blit(save1, [93, 30])
                                            screen.blit(save2, [93, 278])
                                            screen.blit(save3, [93, 526])
                                            screen.blit(button_overlay_1,[83, 516])
                                            overlay_pos2 = 2
                                            pygame.display.flip()
                                        else:
                                            pass
                                    elif event.key == pygame.K_UP:
                                        if overlay_pos2 == 1:
                                            screen.blit(background, [0, 0])
                                            screen.blit(save1, [93, 30])
                                            screen.blit(save2, [93, 278])
                                            screen.blit(save3, [93, 526])
                                            screen.blit(button_overlay_1,[83, 20])
                                            overlay_pos2 = 0 
                                            pygame.display.flip()
                                        elif overlay_pos2 == 2:
                                            screen.blit(background, [0, 0])
                                            screen.blit(save1, [93, 30])
                                            screen.blit(save2, [93, 278])
                                            screen.blit(save3, [93, 526])
                                            screen.blit(button_overlay_1,[83, 268])
                                            overlay_pos2 = 1
                                            pygame.display.flip()
                                        else:
                                            pass
                    elif overlay_pos == 1:
                        print "Options aren't implemented yet. I do confirm there will be a language option. That won't be easy to do..."