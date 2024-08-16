import pygame
import tools_game
from tools_game import *

class Player():
	def __init__ (self, screen):
		self.image = tools_game.shipImg
		self.rect = self.image.get_rect()
		self.rect.center = tools_game.width * 0.5,tools_game.height * 0.94
		self.life = 3
		
	def show(self):
		tools_game.screen.blit(tools_game.shipImg, (self.rect.x, self.rect.y))
		
	def update(self):
		x,y = pygame.mouse.get_pos()
		if x >= 0 and x <= (tools_game.width-57):
			self.rect.x = x
	

	def collide(self,alien_group):
			for alien in alien_group.sprites():
				if pygame.Rect.colliderect(alien.rect,self.rect) == True:
					alien.kill()
					alien_destroy.play()
					self.kill()
					
	
		
		
		



	
