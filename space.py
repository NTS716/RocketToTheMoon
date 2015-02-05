import pygame

class Space():
	def __init__(self, surface):
		self.img = pygame.image.load("./assets/stars1.gif")
		self.img = pygame.transform.scale(self.img, (800,600))
		self.size = (800,600)
		self.pos = (0,0)
		self.surface = surface
	def draw(self):
		self.surface.blit(self.img, self.pos)
		self.surface.blit(self.img, (self.pos[0], (self.pos[1] + 600)))
		self.pos = (self.pos[0], self.pos[1] - 2)
		if self.pos[1] <= -600:
			self.pos = (0,0)
