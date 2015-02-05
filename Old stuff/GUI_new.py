import pygame
from pygame.locals import *
import sys
from colors import *
from Rocket import Rocket 
from Asteroids import Asteroid

def main():
	#Initialize pygame
	pygame.init()

	#Create the display and set the caption
	SCREEN = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Rocket to the Moon")

	#Create the clock object and define frames per second
	clock = pygame.time.Clock()
	fps = 35

	#Create an add text fuction
	def addText(text, size, pos, color):
		font = pygame.font.SysFont('calibri', size)
		text = font.render(text, 0, color)
		SCREEN.blit(text, pos)

	#Create the sprite lists
	allSprites = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	#Define the rocket
	rocket = Rocket()
	allSprites.add(rocket)

	#Define the Asteroids
	for i in range(8):
		asteroid = Asteroid()
		asteroid.shufflePos()
		asteroids.add(asteroid)
		allSprites.add(asteroid)

        #Create the moon
        distanceFromMoon = 300000

        invictory = False

        def victory():
            SCREEN.fill(GREEN)
            addText("You win!!!", 90, (100, 100), BLACK)

        #Create small versions of the rocket at the bottomright of the screen
        def showLives():
            if rocket.lives == 3:
                pygame.draw.rect(SCREEN, WHITE, ((700, 550), (20, 20)))
                pygame.draw.rect(SCREEN, WHITE, ((730, 550), (20, 20)))
                pygame.draw.rect(SCREEN, WHITE, ((760, 550), (20, 20)))
            elif rocket.lives == 2:
                pygame.draw.rect(SCREEN, WHITE, ((730, 550), (20, 20)))
                pygame.draw.rect(SCREEN, WHITE, ((760, 550), (20, 20)))
            elif rocket.lives == 1:
                pygame.draw.rect(SCREEN, WHITE, ((760, 550), (20, 20)))

        #Update everything
	def update():
		SCREEN.fill(BLACK)
                showLives()
		rocket.move()
		for asteroid in asteroids:
			asteroid.fall()
		collideList = pygame.sprite.spritecollide(rocket, asteroids, False)
		if collideList:
			rocket.getHit()
		allSprites.draw(SCREEN)

	def gameOver():
		SCREEN.fill(RED)
		addText("Game Over", 90, (100, 100), BLACK)

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
			    pygame.quit()
			    sys.exit()
                        elif event.type == MOUSEBUTTONDOWN:
                            print pygame.mouse.get_pos()
                if distanceFromMoon <= 0:
                    invictory = True
                if not rocket.gameOver or invictory:
		    update()
                    addText(str(distanceFromMoon), 90, (80, 500), WHITE)
                if rocket.gameOver:
                    gameOver()
                if invictory:
                    victory()
                distanceFromMoon -= 300
		pygame.display.update()
		clock.tick(fps)

if __name__ == '__main__':
	main()
