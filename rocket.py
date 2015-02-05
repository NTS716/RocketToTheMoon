import pygame

class Rocket(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	
		self.image = pygame.image.load("./assets/rocket.png")
		self.image = pygame.transform.scale(self.image, (100, 120))
		self.rect = self.image.get_rect()
