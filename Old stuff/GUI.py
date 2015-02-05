import pygame
from pygame.locals import *
import sys
from random import randint

def main():
    #Initialize Pygame
    pygame.init()

    #Create the display and caption the window
    SCREEN = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Rocket to the Moon")

    #Create the clock object and define the frames per second
    clock = pygame.time.Clock()
    fps = 35

    #Create the rocket
    class Rocket(pygame.sprite.Sprite):
        def __init__(self):
            self.pos = (300, 400)
            self.size = (50, 50)
            self.speed = (1.00, 1.00, 1.00, 1.00)
            self.rect = (self.pos, self.size)

            pygame.sprite.Sprite.__init__(self)

        def draw(self):
            pygame.draw.rect(SCREEN, (255,255,255), (self.pos , self.size)) 

        def move(self):
            #move up
            if pygame.key.get_pressed()[pygame.K_w]:
                self.pos = (self.pos[0], self.pos[1] - self.speed[0])
                self.speed = (self.speed[0] + 0.05, self.speed[1], self.speed[2], self.speed[3])
            else:
                if self.speed[0] > 1.0:
                    self.speed = (self.speed[0] - 0.5, self.speed[1], self.speed[2], self.speed[3])
                elif self.speed[0] < 1.0:
                    self.speed = (1.0, self.speed[1], self.speed[2], self.speed[3])
            #move down
            if pygame.key.get_pressed()[pygame.K_s]:
                self.pos = (self.pos[0], self.pos[1] + self.speed[1])
                self.speed = (self.speed[0], self.speed[1] + 0.05, self.speed[2], self.speed[3])
            else:
                if self.speed[1] > 1.0:
                    self.speed = (self.speed[0], self.speed[1] - 0.05, self.speed[2], self.speed[3]) 
                elif self.speed[1] < 1.0:
                    self.speed = (self.speed[0], 1.0, self.speed[2], self.speed[3])
            #move right
            if pygame.key.get_pressed()[pygame.K_d]:
                self.pos = (self.pos[0] + int(self.speed[2]), self.pos[1])
                self.speed = (self.speed[0], self.speed[1], self.speed[2] + 0.05, self.speed[3])
            else:
                if self.speed[2] > 1.0:
                    self.speed = (self.speed[0], self.speed[1], self.speed[2] - 0.05, self.speed[3])
                elif self.speed[2] < 1.0:
                    self.speed = (self.speed[0], self.speed[1], 1.0, self.speed[3])
            #move left
            if pygame.key.get_pressed()[pygame.K_a]:
                self.pos = (self.pos[0] - int(self.speed[3]), self.pos[1])
                self.speed = (self.speed[0], self.speed[1], self.speed[2], self.speed[3] + 0.05)
            else:
                if self.speed[3] > 1.0:
                    self.speed = (self.speed[0], self.speed[1], self.speed[2], self.speed[3] - 0.05)
                elif self.speed[3] < 1.0:
                    self.speed = (self.speed[0], self.speed[1], self.speed[2], 1.0)

    rocket = Rocket()

    #Create the asteroid
    class Asteroid(pygame.sprite.Sprite):
        def __init__(self):
            self.size = randint(20, 120) 
            self.pos = (randint(0, 700), randint(-600, 0))
            self.image = pygame.Surface((self.size, self.size))
            self.image.fill((255,0,0))
            self.rect = self.image.get_rect()

            pygame.sprite.Sprite.__init__(self)

        def scroll(self):
            self.pos = (self.pos[0], self.pos[1] + 3)
        def rePos(self):
            if self.pos[1] > 600:
                self.pos = (randint(0, 700), randint(-600, 0))
            
    asteroids = pygame.sprite.Group()
    for i in range(8):
        asteroid = Asteroid()
        asteroids.add(asteroid)

    #Main pygame loop
    while True:
        SCREEN.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        rocket.draw()
        rocket.move()
        asteroids.draw(SCREEN)
        for asteroid in asteroids:
            asteroid.scroll()
            asteroid.rePos()
            print asteroid.rect.width
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    main()
