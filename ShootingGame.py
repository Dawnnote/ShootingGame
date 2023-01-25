import pygame
import sys
import random
from time import sleep

BLACK=(0,0,0)
padWidth = 480  #게임화면 크기
padHeight = 640 

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

def drawObject(obj, x, y):
    global gamePad
    

# 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad

# 운석이 화면 아래로 통과한 개수
def writePassed(count):
    global gamePad

# 게임 메시지 출력
def writeMessage(text):
    global gamePad, gameOverSound

# 전투기가 운석과 충돌했을 때 메시지 출력
def crash():
    global gamePad

# 게임 오버 메시지 보이기
def gameOver():
    global gamePad