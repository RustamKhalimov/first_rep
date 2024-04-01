import pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((512,512))
screen.fill("white") 
counter = 0
done = True
index = 0
playlist = ['Music`s/Кайрат Нуртас - Журегиннен бир орын бер бос болса 2017-[muzmir.kz].mp3',
            'Music`s/bambee-bumble-bee-mp3',
            'Music`s/Думан Марат - Жіберем қалай (2022) [muzik.kz].mp3',
            'Music`s/Bejbit_Korgan_Zhanary_ottaj_zhanyp_zhuregimdi_shoқtaj_қaryp.mp3',
            'Music`s/Jah Khalib-Созвездие Ангела/mp3',
            'Music`s/Kairat Nurtas – Seni Suiem.mp3',
            'Music`s/Psy - Gangnam Style.mp3',
            'Music`s/V $ X V PRiNCE & DE LACURE - Big City Life.mp3'
            ]
pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play()

pause = True
while done:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_d:
                index = index + 1
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_a:
                index = index - 1
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if pause == False:
                pygame.mixer.music.pause()
                screen.fill("white") 
                
            if pause == True:
                pygame.mixer.music.unpause()
                screen.fill("white") 
                
        if event.type == pygame.QUIT:
            done = False
            pygame.quit()
            break