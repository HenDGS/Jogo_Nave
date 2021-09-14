import pygame
import sys
from bullet import Bullet
from settings import *


def check_event(nave,bullets,settings,screen):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				nave.moving_right=True
			elif event.key==pygame.K_LEFT:
				nave.moving_left=True
			elif event.key==pygame.K_SPACE:
				new_bullet=Bullet(settings,screen,nave)
				bullets.add(new_bullet)
		
		elif event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT:
				nave.moving_right=False
			elif event.key==pygame.K_LEFT:
				nave.moving_left=False
				
		
	
	
			
def update_screen(config,screen,nave,bullets):
		screen.fill(config.cor_fundo)
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		nave.blitme()
			
		pygame.display.flip()
		
	
