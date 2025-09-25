import pygame

from constants import *
from player import *
from asteroid import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroid = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroid, updatable, drawable)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen : {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        
        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000     

if __name__ == "__main__":
    main()