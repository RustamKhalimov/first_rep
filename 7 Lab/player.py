import pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((512,512))
screen.fill("white") 
counter = 0
runer = True
index = 0
playlist = [r"C:\Users\RHali\Downloads\Кайрат Нуртас – Алматының Түндер-Ай.mp3",
            r"C:\Users\RHali\Downloads\Кайрат Нуртас – Ауырмайды Жүрек (1).mp3",
            r"C:\Users\RHali\Downloads\Кайрат Нуртас – Жубатуга Арналады Бул Аним.mp3",
            r"C:\Users\RHali\Downloads\Кайрат Нуртас – Сұранамын.mp3",
            r"C:\Users\RHali\Downloads\Kairat Nurtas – Қызыл гүлім-ай.mp3",
            r"C:\Users\RHali\Downloads\Кайрат Нуртас – Ауырмайды Жүрек.mp3",
            r"C:\Users\RHali\Downloads\Kairat Nurtas – Seni Suiem.mp3",
            r"C:\Users\RHali\Downloads\Bejbit_Korgan_Zhanary_ottaj_zhanyp_zhuregimdi_shoқtaj_қaryp.mp3"
            ]
pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play()

pause = True
while runer:
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
            runer = False
            pygame.quit()
            break