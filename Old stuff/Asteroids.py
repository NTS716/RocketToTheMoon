import pygame
from colors import *
from random import randint
class Asteroid(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.size = randint(20, 120)

		self.image = pygame.Surface((self.size, self.size))
		self.image.fill(RED)
		
		self.rect = self.image.get_rect()

	def shufflePos(self):
		self.rect.x = randint(0, 700) 
		self.rect.y = randint(-600, 0)

	def fall(self):
		self.rect.y += 3
		if self.rect.y > 600:
			self.shufflePos() 
