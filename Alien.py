import pygame
from tools_game import *
import random

class Alien (pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		
		self.image = alienImg
		self.rect = self.image.get_rect()
		self.rect.center = x,y
		
			 
class Alien_group(pygame.sprite.Group):
	def __init__(self,x, y, width, height, level):
		super().__init__()
		
		self.direction = 10 * (level*0.25)
		
		X = x
		Y = y
		for i in range(5):
			for j in range(7):
				Alien(X,Y).add(self)
				X += width + (width/ 200.0)
			Y += height + (height / 7.0)
			X = x	
						
						
	def update(self):
		for alien in self.sprites():
			alien.rect.x += self.direction
			if alien.rect.right >= width or alien.rect.left <= 0:
				self.direction  *= -1
				self.update_down()
	
				
	def update_down(self):
		for alien in self.sprites():
			alien.rect.y += 20
						
	def get_alien_random(self):
		alien_array = []
		for alien in self.sprites():
			alien_array.append(alien)
		if len(alien_array) > 0:
			alien_shoot = random.choice(alien_array)
			return alien_shoot
		
		
			




	
