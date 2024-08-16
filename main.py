import pygame
from pygame import mixer
import Alien 	
import fire
from Player import *
from tools_game import *



class main:

	level = 1
	score = 0
	lives = 3
	
	crashed = False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
				
		
		textLevel = font.render('LEVEL: '+str(level), True, (255,255,255), )
		textRectLevel = textLevel.get_rect()
		textRectLevel.center = (width * 0.06, height * 0.04	)
		textRectLevel.y = (height * 0.05)
		textRectLevel.x = (width * 0.03)			

		bgSound.play()
		
		ship = Player(screen)
		alien_group = Alien.Alien_group(100,25,150,50,level)
		rapid_fire = fire.Rapid_fire(screen)
		
		crashed = False
		while not crashed:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					crashed = True
		
			textScore = font.render('SCORE: '+str(score), True, (255,255,255), )
			textRectScore = textScore.get_rect()
			textRectScore.y = (height * 0.1)
			textRectScore.x = (width * 0.03)

			textLives = font.render('LIVES: '+str(lives), True, (255,255,255), )
			textRectLives = textLives.get_rect()
			textRectLives.y = (height * 0.15)
			textRectLives.x = (width * 0.03)
		
			if len(alien_group) == 0:	
				level += 1
				lives += 3
				LevelUp.play()				
				break
				
			if lives == 0:
				print("GAME OVER")
				quit()

			screen.blit(bg,(0, 0))
			screen.blit(textLevel, textRectLevel)
			screen.blit(textScore, textRectScore)
			screen.blit(textLives, textRectLives)
			ship.show()
			ship.update()
			
			alien_group.draw(screen)
			alien_group.update()
			
			alien_shoot = alien_group.get_alien_random()
			rapid_fire.alien_shoot(alien_shoot)
			
			rapid_fire.click(ship.rect.center[0],ship.rect.center[1]-50)
			rapid_fire.update()
			rapid_fire.draw(screen)
			
			a,b= rapid_fire.collide(alien_group,ship,level,lives)
			score += a
			lives -= b
			
			ship.collide(alien_group)
		   	
			pygame.display.update()
			clock.tick(25)

	pygame.quit()
	quit()

if __name__=="__main__":
	main()

	
