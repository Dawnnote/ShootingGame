import pygame
import sys
import random
from time import sleep

BLACK=(0,0,0)
padWidth = 480  #게임화면 크기
padHeight = 640 

def initGame():
    global gamePad, clock, background, fighter, missile, explosion, missileSound, gameOverSound

def runGame():
    global gamepad, clock, background, fighter, missile, explosion, missileSound
 
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
