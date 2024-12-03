import pygame
import time

pygame.init()
screen=pygame.display.set_mode((800,600))
red_rocket=pygame.image.load('Space_Shooter Jetlearn/Red_Rocket.png')
yellow_rocket=pygame.image.load('Space_Shooter Jetlearn/Rocket_Yellow.png')
background=pygame.image.load('Space_Shooter Jetlearn/Backround.png')

backgroundnew=pygame.transform.scale(background,(800,600))
rocket_red=pygame.transform.rotate(pygame.transform.scale(red_rocket,(55,40)),270)





playing=True
clock=pygame.time.Clock()
while playing==True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.blit(backgroundnew,(0,0))
    screen.blit(rocket_red,(575,250))



    pygame.display.update()            

            