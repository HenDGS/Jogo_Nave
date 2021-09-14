import sys
import pygame
from settings import *
from nave import *
import eventos as inp
from pygame.sprite import Group

def run_game():
	config=Settings()
	pygame.init()
	screen=pygame.display.set_mode((config.screen_width,config.screen_height))
	pygame.display.set_caption("Futuro Orange Juice Collector Remake")
	
	bullets=Group()
	nave=Ship(screen,config.speed)
	
	while True:
		"""for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()"""
		inp.check_event(nave,bullets,config,screen)
		nave.update()
		bullets.update()
		inp.update_screen(config,screen,nave,bullets)
			
		screen.fill(config.cor_fundo)
		nave.blitme()
			
		pygame.display.flip()
		
run_game()
