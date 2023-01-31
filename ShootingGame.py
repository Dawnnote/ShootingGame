import pygame
import sys
import random
from time import sleep

BLACK=(0,0,0)
padWidth = 480  #게임화면 크기
padHeight = 640 
rockImage = ['rock01.png','rock02.png','rock03.png','rock04.png','rock05.png',
            'rock06.png','rock07.png','rock08.png','rock09.png','rock10.png',
            'rock11.png','rock12.png','rock13.png','rock14.png','rock15.png',
            'rock16.png','rock17.png','rock18.png','rock19.png','rock20.png',
            'rock21.png','rock22.png','rock23.png','rock24.png','rock025.png',
            'rock26.png','rock27.png','rock28.png','rock29.png','rock30.png',]

def initGame():
    global gamePad, clock, background, fighter, missile, explosion, missileSound, gameOverSound
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')            # 게임 이름
    background = pygame.image.load('background.png')    # 배경 그림
    fighter = pygame.image.load('fighter.png')          # 전투기 그림
    missile = pygame.image.load('missile.png')          # 미사일 그림
    explosion = pygame.image.load('explosion.png')      # 폭발 그림
    pygame.mixer.music.load('musix.wav')                # 배경 음악
    pygame.mixer.music.play(-1)                         # 배경 음악 재생
    missileSound = pygame.mixer.Sound('missle.wav')     # 미사일 사운드
    gameOverSound = pygame.mixer.Sound('gameover.wav')  # 게임 오버 사운드
    clock = pygame.time.Clock()

def runGame():
    global gamepad, clock, background, fighter, missile, explosion, missileSound

    # 무기 좌표 리스트 
    missileXY = []

    # 운석 랜덤 생성 
    rock = pygame.image.load(random.choice(rockImage)) 
    rockSize = rock.get_rect().size # 운석크기 
    rockWidth = rockSize[0] 
    rockHeight = rockSize[1] 

    # 운석 초기 위치 설정 
    rockX = random.randrange(0, padHeight, - rockWidth) 
    rockY =0 
    rockSpeed = 0 


    # 전투기 크기 
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0] 
    fighterHeight = fighterSize[1]

    #전투기 초기 위치 
    x = padWidth * 0.45
    y = padHeight * 0.9 
    fighterX = 0 

    # 전투기 미사일에 운석이 맞았을 경우 True 
    isShot = False 
    shotCount = 0 
    rockPassed = 0 

    onGame =False 

    while not onGame: 
        for event in pygame.event.get(): 
            if event.type in [pygame.QUIT]:
                sys.exit() 

            if event.type in [pygame.KEYDOWN] : 
                if event.key == pygame.K_LEFT : 
                        fighterX -= 5

                elif event.key == pygame.K_RIGHT :
                    fighterX += 5 

                elif event.key == pygame.K_SPACE :
                        missileX = x + fighterWidth/2 
                        missileY = y - fighterHeight
                        missileXY.append([missileX , missileY])

            if event.type in [pygame.KEYUP] : 
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0 

        # 배경화면 그리기 
        drawObject(background, 0,0) 

        # 전투기 위치 재조정 
        x += fighterX 
        if x <0: 
            x=0
        elif x > padWidth - fighterWidth :
            x = padWidth - fighterWidth

        # 비행기를 게임 화면의 (x,y) 좌표에 그림
        drawObject(fighter, x, y)

        #미사일 발사 화면에 그리기 
        if len(missileXY) != 0 : 
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10 
                missileXY[i][1] = bxy[1]

                # 미사일이 운석을 맞추었을 경우 
                if bxy[1] < rockY : 
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy) 
                        isShot = True
                        shotCount += 1

                # 미사일이 화면 밖으로 나가면 
                if bxy[1] <= 0 : 
                    try : 
                        missileXY.remove(bxy)  # 미사일 제거
                    except : 
                        pass 

        if len(missileXY) != 0 : 
            for bx ,by in missileXY : 
                drawObject(missile, bx, by)
                
        # 운석 아래로 움직임 
        rockY += rockSpeed

        # 운석이 지구로 떨어진 경우 
        if rockY > padHeight: 
            # 새로운 운석
            rock= pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size # 운석크기 
            rockWidth = rockSize[0] 
            rockHeight = rockSize[1] 
            rockX = random.randrange(0, padHeight, - rockWidth) 
            rockY =0 

        # 운석을 맞춘 경우 
        if isShot : 
            # 운석 폭발 
            drawObject(explosion , rockX , rockY) 
            # 새로운 운석
            rock= pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size # 운석크기 
            rockWidth = rockSize[0] 
            rockHeight = rockSize[1] 
            rockX = random.randrange(0, padHeight, - rockWidth) 
            rockY =0 
            isShot =False


        # 운석 그리기 
        drawObject(rock, rockX, rockY) 

        # 게임화면을 다시 그림
        pygame.display.update()

        clock.tick(60) 
    
    pygame.quit()



def drawObject(obj, x, y):
    global gamePad
    

# 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
 
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj,(x,y))
    
 
# 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font("NanumGothic.ttf",20)
    text = font.render("파괴한 운석 수:", str(count), True, (255,255,255))
    gamePad.blit(text, (10,0))

# 운석이 화면 아래로 통과한 개수
def writePassed(count):
    global gamePad

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