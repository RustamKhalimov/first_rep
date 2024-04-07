import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60
paused = True
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = True
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)
game_paddle_fonts = pygame.font.SysFont('comicsansms', 50)
game_paddle_text = game_paddle_fonts.render(f'Paddle weight: {paddleW}',True, (255 , 255 , 255))

#Ball
ballRadius = 20
game_ballR_fonts = pygame.font.SysFont('comicsansms', 50)
game_ballR_text = game_ballR_fonts.render(f'Ball radius: {ballRadius}',True, (255 , 255 , 255))
ballSpeed = 6
game_ballS_fonts = pygame.font.SysFont('comicsansms', 50)
game_ballS_text = game_ballS_fonts.render(f'Ball speed: {ballSpeed}',True, (255 , 255 , 255))
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_text2 = game_score_fonts.render(f'Settings:', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Pause
game_paused_fonts = pygame.font.SysFont('comicsansms', 100)
game_paused_text = game_paused_fonts.render(f'Paused',True, (255 , 255 , 255))

#Game change instruction text
game_instruction_fonts = pygame.font.SysFont('comicsansms', 20)
game_instruction_text = game_instruction_fonts.render(f'Instruction of changes:',True,(255 , 255 , 255))
game_ball_radius_change = game_instruction_fonts.render(f'If you press W radius of ball will increase to 1 or if you press S radius of ball will decrease to 1',True, (255 , 255 , 255))
game_ball_speed_change = game_instruction_fonts.render(f'If you press P speed of ball will increase to 1 or if you press O speed of ball will decrease to 1',True, (255 , 255 , 255))
game_paddle_weight_change = game_instruction_fonts.render(f'If you press D weight of paddle will increase to 50 or if you press A weight of paddle will decrease to 50',True, (255 , 255 , 255))
#Catching sound
collision_sound = pygame.mixer.Sound('Voices/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 
print(block_list)

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
settings = losefont.render('Game Over', True, (255, 255, 255))
settingsrect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)
settingsrect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)


while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
                pygame.display.update()
        if not paused:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ballRadius = ballRadius + 1
                    game_ballR_text = game_ballR_fonts.render(f'Ball radius: {ballRadius}',True, (255 , 255 , 255))
                elif event.key == pygame.K_s:
                    ballRadius = ballRadius - 1                  
                    game_ballR_text = game_ballR_fonts.render(f'Ball radius: {ballRadius}',True, (255 , 255 , 255))
                elif event.key == pygame.K_d:
                    paddleW = paddleW + 50
                    paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)
                    game_paddle_text = game_paddle_fonts.render(f'Paddle weight: {paddleW}',True, (255 , 255 , 255))
                elif event.key == pygame.K_a:
                    paddleW = paddleW - 50
                    paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)
                    game_paddle_text = game_paddle_fonts.render(f'Paddle weight: {paddleW}',True, (255 , 255 , 255))
                elif event.key == pygame.K_p:
                    ballSpeed = ballSpeed + 1
                    game_ballS_text = game_ballS_fonts.render(f'Ball speed: {ballSpeed}',True, (255 , 255 , 255))
                elif event.key == pygame.K_o:
                    ballSpeed = ballSpeed - 1
                    game_ballS_text = game_ballS_fonts.render(f'Ball speed: {ballSpeed}',True, (255 , 255 , 255))

                
    screen.fill(bg)
    
    # print(next(enumerate(block_list)))
    if paused:
        [pygame.draw.rect(screen, color_list[color], block)
        for color, block in enumerate (block_list)] #drawing blocks
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    # print(next(enumerate (block_list)))

    #Ball movement
    if paused:
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

    #Something like Pause menu
    if not paused:
        screen.blit(game_paused_text,( W//2-150 , H//2-400))
        screen.blit(game_ballR_text,(100,200))
        screen.blit(game_ballS_text,(100,270))
        screen.blit(game_paddle_text,(100,330))
        screen.blit(game_instruction_text,(100,450))
        screen.blit(game_ball_radius_change,(100,500))
        screen.blit(game_ball_speed_change,(100,550))
        screen.blit(game_paddle_weight_change,(100,600))


    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision blocks
    hitIndex = ball.collidelist(block_list)
    
    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()
        
    #Game score
    if paused:
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)

        
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
    
    #Paddle Control
    if paused:
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed


    pygame.display.flip()
    clock.tick(FPS)