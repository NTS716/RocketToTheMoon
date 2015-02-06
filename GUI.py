import pygame
from pygame.locals import *
import sys
from colors import *
from space import Space
from rocket import Rocket
from Buttons import Button
from asteroids import Asteroid

def main():
    #Initialize Pygame
    pygame.init()

    #Create the display and caption the window
    SCREEN = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Rocket to the Moon")

    #Create the clock object and fps
    clock = pygame.time.Clock()
    fps = 60

    #Initialize phase
    phase = 0

    #Create an addText function
    def addText(text, pos, size, color):
        FONT = pygame.font.SysFont('calibri', size)
        TEXT = FONT.render(text, 5, color)
        SCREEN.blit(TEXT, pos)

    #Create the sprite lists
    allSprites = pygame.sprite.Group()
    rocket_list = pygame.sprite.Group() # This is a sloppy sprite list made for the intro for the rocket.
    asteroids = pygame.sprite.Group()

    #Create an instance of the background
    space = Space(SCREEN)

    #Create the rocket
    rocket = Rocket()
    allSprites.add(rocket)
    rocket_list.add(rocket)

    #Create the lives images
    life = pygame.image.load("./assets/rocket.png")
    life = pygame.transform.scale(life, (20, 30))
    def showLives():
        if rocket.lives == 3:
            SCREEN.blit(life, (700, 550))
            SCREEN.blit(life, (740, 550))
            SCREEN.blit(life, (780, 550))
        elif rocket.lives == 2:
            SCREEN.blit(life, (740, 550))
            SCREEN.blit(life, (780, 550))
        elif rocket.lives == 1:
            SCREEN.blit(life, (780, 550))

    #Create the asteroids
    for i in range(8):
        asteroid = Asteroid()
        allSprites.add(asteroid)
        asteroids.add(asteroid)  
        asteroid.shuffle()

    #Create the intro buttons
    playButton = Button(SCREEN, 'rect', (165, 485), (150, 75), GREEN)
    quitButton = Button(SCREEN, 'rect', (485, 485), (150, 75), RED)

    def buttons():
        playButton.draw()
        quitButton.draw()
        playButton.addText('Play', 'calibri', 40, (0,0,0))
        quitButton.addText('Quit', 'calibri', 40, (0,0,0))
        #When the mouse touches the play button
        if playButton.touching(pygame.mouse.get_pos()):
            playButton.detail = (0,150,0)
        else:
            playButton.detail = GREEN
            playButton.bevel((0,150,0), 5, ['left', 'bottom'])
        #When the mouse touches the quit button
        if quitButton.touching(pygame.mouse.get_pos()):
            quitButton.detail = (150, 0, 0)
        else:
            quitButton.detail = RED
            quitButton.bevel((150,0,0), 5, ['left', 'bottom'])

    #Create the intro
    def intro():
        addText("Rocket", (270, 100), 100, RED)
        addText("to the", (230, 200), 60, BLUE)
        addText("Moon", (350, 175), 120, GREEN)
        buttons()

    #Create the startGame 
    def startGame():
        rocket.rect.x = 350
        rocket.rect.y = 600

    def rocketIntro():
        rocket_list.draw(SCREEN)
        if rocket.rect.y != 500:
            rocket.rect.y -= 2

    def play():
        rocket.move()
        for asteroid in asteroids:
            asteroid.scroll()
        allSprites.draw(SCREEN)
        showLives()

    #Main pygame loop
    while True:
        space.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if phase == 0 and quitButton.touching(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                if phase == 0 and playButton.touching(pygame.mouse.get_pos()):
                    phase = 1
                    startGame()
        if phase == 0:
            intro()
        elif phase == 1:
            rocketIntro()
            if rocket.rect.y == 500:
                phase = 2
        elif phase == 2:
            play()
            collideList = pygame.sprite.spritecollide(rocket, asteroids, False)
            if collideList:
                rocket.explode()
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    main()
