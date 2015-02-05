import pygame
from pygame.locals import *
import sys
from colors import *
from space import SPACE
from Buttons import Button

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
        pass

    #Main pygame loop
    while True:
        SCREEN.blit(SPACE, (0,0))
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
        if phase == 0:
            intro()
        elif phase == 1:
            startGame()
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    main()
