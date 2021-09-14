import pygame

class Ship():
	
	def __init__(self,screen,speed):
		self.screen=screen
		
		self.image=pygame.image.load("images/ship.bmp")
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		
		self.center=float(self.screen_rect.centerx)
		
		self.moving_right=False
		self.moving_left=False
		
		self.speed=speed
	
	def update(self):
		if self.moving_right + self.rect.right>self.screen_rect.right:
			self.center=self.screen_rect.left+48
		elif self.moving_left + self.rect.left<self.screen_rect.left:
			self.center=self.screen_rect.right-48
		elif self.moving_right:
			self.center+=self.speed
		elif self.moving_left:
			self.center-=self.speed
		
		self.rect.centerx=self.center
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
