import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1000 , 800) , pygame.RESIZABLE)
done = True
x = 500
y = 400
clock = pygame.time.Clock()
screen.fill((255 ,255 , 255))
pygame.display.update()
while done:
    screen.fill((255 , 255 , 255))
    cercle1 = pygame.draw.circle(screen, (255 , 0 , 0), (x , y), 25 ,width=0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x > 50 :
                    x = x - 20
            elif event.key == pygame.K_RIGHT:
                if x < 950:
                    x = x + 20
            elif event.key == pygame.K_UP:
                if y > 50:
                    y = y - 20
            elif event.key == pygame.K_DOWN:
                if y < 740:
                    y = y + 20
    pygame.display.update()
    clock.tick(60)