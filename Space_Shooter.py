import pygame
import time

pygame.init()
screen=pygame.display.set_mode((800,600))
red_rocket=pygame.image.load('Space_Shooter Jetlearn/Red_Rocket.png')
yellow_rocket=pygame.image.load('Space_Shooter Jetlearn/Rocket_Yellow.png')
background=pygame.image.load('Space_Shooter Jetlearn/Backround.png')

backgroundnew=pygame.transform.scale(background,(800,600))
rocket_red=pygame.transform.rotate(pygame.transform.scale(red_rocket,(55,40)),270)
rocket_yellow=pygame.transform.rotate(pygame.transform.scale(yellow_rocket,(55,40)),90)
rocket_sound=pygame.mixer.Sound('Space_Shooter Jetlearn\Grenade+1.mp3')




def red_movement(keys_pressed,rocket_red):
    if keys_pressed[pygame.K_UP] and red.y >0:
        red.y-=5
    if keys_pressed[pygame.K_DOWN] and red.y <600:
        red.y+=5

    if keys_pressed[pygame.K_LEFT] and red.x >400:
        red.x-=5

    if keys_pressed[pygame.K_RIGHT] and red.x <800:
        red.x+=5   


###
def yellow_movement(keys_pressed,rocket_yellow):
    if keys_pressed[pygame.K_w] and yellow.y>0:
        yellow.y-=5

    if keys_pressed[pygame.K_s] and yellow.y <600:
        yellow.y+=5

    if keys_pressed[pygame.K_a] and yellow.x >0:
        yellow.x-=5

    if keys_pressed[pygame.K_d] and yellow.x <360:
        yellow.x+=5




    

BORDER = pygame.Rect(800//2,0,10,600)

red_bullets = []
yellow_bullets = []




playing=True
clock=pygame.time.Clock()
yellow = pygame.Rect(100,300,55,40)
red = pygame.Rect(575,300,55,40)
while playing==True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        ##creating bullets

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                bullet=pygame.Rect(yellow.x,yellow.y,10,5)
                yellow_bullets.append(bullet)
                rocket_sound.play()





    screen.blit(backgroundnew,(0,0))
    screen.blit(rocket_red,(red.x,red.y))
    screen.blit(rocket_yellow,(yellow.x,yellow.y))




    pygame.draw.rect(screen,'gray0',BORDER)

    keys_pressed = pygame.key.get_pressed()
    red_movement(keys_pressed,red)

    yellow_movement(keys_pressed,yellow)
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,'darkGoldenrod',bullet)
        bullet.x+=5


    pygame.display.update()            

            
