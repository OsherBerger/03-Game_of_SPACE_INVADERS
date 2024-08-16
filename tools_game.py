import pygame
from pygame.locals import *
from pygame import mixer


#file tools_game:
pygame.init()
clock = pygame.time.Clock()
size_screen = width,height = 1280,720

screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption('Space Invaders') 

#load image
bg = pygame.image.load('image/space.png')
shipImg = pygame.image.load('image/ship.bmp')
shipImg = pygame.transform.scale(shipImg,(35,60))

fireImg = pygame.image.load('image/fire.png')
alienImg = pygame.image.load('image/alien.bmp')
alienImg = pygame.transform.scale(alienImg,(50,25))
#gameOverImg = pygame.image.load('')
font = pygame.font.Font('font/Kid Games.ttf', 32)



bgSound = pygame.mixer.Sound('music/space.wav')
bgSound.set_volume(0.5)

soundFire =  pygame.mixer.Sound('music/laser.wav')
soundFire.set_volume(0.2)

deadPlayer =  pygame.mixer.Sound('music/deadPlayer.wav')
deadPlayer.set_volume(0.8)

LevelUp =  pygame.mixer.Sound('music/level-up.wav')
LevelUp.set_volume(0.8)

alien_destroy =  pygame.mixer.Sound('music/alien_destroy.wav')
alien_destroy.set_volume(0.2)


	
