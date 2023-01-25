# 게임 메세지 출력
def writeMessage(text):
    global gamePad, gameoverSound
    textfont = pygame.font.Font('NanumGothic.ttf', 80)
    text = textfont.render(text,True,(255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text,textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameoverSound.play()
    sleep (2)
    pygame.mixer.music.play(-1) # 배경 음악 재생
    runGame()

# 전투기가 운석과 충돌했을 때
def crash():
    global gamePad
    writeMessage('전투기 파괴!')


# 게임 오버 메시지
def gameOver():
    global gamePad
    writeMessage('게임 오버!')
