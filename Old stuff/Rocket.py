import pygame
from colors import *
import sys

class Rocket(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((50, 50)) #Create a blank pygame surface 50x50
		self.image.fill(WHITE)
		
		self.rect = self.image.get_rect()

		self.speeds = [1.0, 1.0, 1.0, 1.0]
                
                self.lives = 3
                self.gameOver = False

                self.rect.x = 300
                self.rect.y = 500

	def pressing(self, key):
		if pygame.key.get_pressed()[key]:
			return True
		else:
			return False
	
	def accelerate(self, speed):
		self.speeds[speed] += 0.02	
	
	def decelerate(self, speed):
		if self.speeds[speed] > 1.0:
			self.speeds[speed] -= 0.03
	
	def move(self):

		if self.pressing(pygame.K_w):
			self.rect.y -= int(self.speeds[0])
			self.accelerate(0)
		else:
			self.decelerate(0)

		if self.pressing(pygame.K_s):
			self.rect.y += int(self.speeds[1])
			self.accelerate(1)
		else:
			self.decelerate(1)

		if self.pressing(pygame.K_d):
			self.rect.x += int(self.speeds[2])
			self.accelerate(2)
		else:
			self.decelerate(2)

		if self.pressing(pygame.K_a):
			self.rect.x -= int(self.speeds[3])
			self.accelerate(3)
		else:
			self.decelerate(3)

        def getHit(self):
            if self.lives > 1:
                self.lives -= 1
                self.rect.x = 300
                self.rect.y = 500
            else:
                self.gameOver = True
