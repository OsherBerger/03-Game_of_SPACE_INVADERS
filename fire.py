import pygame
from tools_game import *



class Bullet(pygame.sprite.Sprite):
	def __init__(self,x,y,direction):
		super().__init__()
		self.image = fireImg
		self.rect = self.image.get_rect()
		self.rect.center = x,y
		self.direction = direction
		
		
	def update(self):
		self.rect.y += self.direction
		if self.rect.y <= 0 or self.rect.y >= height :
			self.kill()
			
		
	
class Rapid_fire(pygame.sprite.Group):
	def __init__(self,screen):
		super().__init__()
		self.screen = screen
		self.time1 = pygame.time.get_ticks()
		self.time2 = pygame.time.get_ticks()
		
	def click(self,x,y):
		mouse_key = pygame.mouse.get_pressed()	
		now_time = pygame.time.get_ticks()
		if mouse_key[0] == True and (now_time - self.time1) > 100:# (2nd way to limit fire amount) and len(self.sprites()) < 5 :	
			soundFire.play()	
			Bullet(x, y,-10).add(self)
			self.time1 = pygame.time.get_ticks()
			
	
			
	def collide(self,alien_group,ship,level,lives):
		a = 0 
		b = 0
		for alien in alien_group.sprites():
			for bullet in self.sprites():
				if pygame.Rect.colliderect(alien.rect,bullet.rect):
					if bullet.direction < 0:							
						alien.kill()
						alien_destroy.play()
						bullet.kill()
						a+= 10 * level
						
				if pygame.Rect.colliderect(ship.rect,bullet.rect):			
					if bullet.direction > 0:
						b += 1
						bullet.kill()
						deadPlayer.play()
		return a,b
												
			
	def alien_shoot(self,alien):
		now_time = pygame.time.get_ticks()
		location_alien = alien.rect
		x,y,w,h = location_alien		
		if (now_time - self.time2) > 200 :	
			Bullet(x,y,10).add(self)
			self.time2 = pygame.time.get_ticks()

	
