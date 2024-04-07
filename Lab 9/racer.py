import pygame
import random
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((840,650))
done = True
pygame.display.set_caption('Race project')
x = 178
y = 510
c = 15
d = 0
score = 0
score_2 = 0
anemy_cars_speed = 5
#Score size
font_score = pygame.font.SysFont('Arial' , 26 , bold = True)
#Coordinates for cars and coins
rows_cor = [178,295,424,555]
game = True
#Pictures
track = pygame.image.load('pictures/track.png')
main_car = pygame.image.load('pictures/Main_car.png')
green_car = pygame.image.load('pictures/Green_car.png')
Game_over = pygame.image.load('pictures/Game_Over.png')
Coin = pygame.image.load('pictures/Coin.png')
#Generation time to cars and coins
start_time1 = pygame.time.get_ticks()
start_time2 = pygame.time.get_ticks()
state = pygame.key.get_pressed()
#Coin Pick Sound
coin_pick = pygame.mixer.music.load('Voices/Coin_Pick.mp3')
cars = []
coins = []
while done:
    screen.blit(track,(0,0))
    screen.blit(main_car , (x,y))
    render_score = font_score.render(f'Your score: {score}',1,'Black')
    screen.blit(render_score , (700,0))
    if game:
        if pygame.time.get_ticks()-start_time1>1000:
            random_int1 = random.choice(rows_cor)
            cars.append([random_int1,0])
            start_time1 = pygame.time.get_ticks()
        if pygame.time.get_ticks()-start_time2>3300:
            random_int2 = random.choice(rows_cor)
            coins.append([random_int2,0])
            start_time2 = pygame.time.get_ticks()
    if game:
        for car in cars:
            screen.blit(green_car ,(car[0],car[1]))
            car[1] = car[1] + anemy_cars_speed
        for coin in coins:
            screen.blit(Coin,(coin[0],coin[1]))
            coin[1] = coin[1] + 7
    
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    state = pygame.key.get_pressed()            
    
    if state[pygame.K_RIGHT]:
        if x < 590:
            x = x + c
    if state[pygame.K_LEFT]:
        if x > 170:
            x = x - c
    if state[pygame.K_UP]:
        if y > 50:
            y = y - c
    if state[pygame.K_DOWN]:
        if y < 510:
            y = y + c
    
    for coin in coins:
        if (x <= coin[0] <= x + 57 or coin[0] <= x <= coin[0] + 57) and (y <= coin[1] <= y + 57 or coin[1] <= y <= coin[1] + 57):
            score += 1
            score_2 += 1
            coins.remove(coin)
            pygame.mixer.music.play()
    
    #each 5 coin increase anemy_cars_speed to 1
    if score_2 != 0 and score_2 % 5 == 0:
        anemy_cars_speed = anemy_cars_speed + 1
        score_2 = 0
            
            
    for car in cars:
        if abs(x-car[0])<=57 and abs(y-car[1])<=120:
            game = False
            screen.blit(Game_over,(70,20))
            pygame.display.update
            c = 0
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            pygame.quit()
    clock.tick(60)
    pygame.display.flip()
    