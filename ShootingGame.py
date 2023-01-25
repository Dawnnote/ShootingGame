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