import pygame
import sys

class Rocket(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	
		self.image = pygame.image.load("./assets/rocket.png")
	#	self.image = pygame.transform.scale(self.image, (100, 120))
		self.rect = self.image.get_rect()

		self.lives = 3

	#Method checks if a key is being pressed
	def pressing(self, key):
		if pygame.key.get_pressed()[key] != 0:
			return True
		else:
			return False
	#Method controls the rocket's movement
	def move(self):
		if self.pressing(pygame.K_w) and self.rect.y >= 0:
			self.rect.y -= 3
		if self.pressing(pygame.K_s) and self.rect.y <= 500:
			self.rect.y += 3
		if self.pressing(pygame.K_a) and self.rect.x >= 0:
			self.rect.x -= 3
		if self.pressing(pygame.K_d) and self.rect.x <= 700:
			self.rect.x += 3
	#What happens when you die
	def explode(self):
		if self.lives > 1:
			self.lives -= 1
			self.rect.x = 350
			self.rect.y = 500
		else:
			pygame.quit
			sys.exit()
