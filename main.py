import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        # quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # black out screen
        screen.fill("black")
        # update and draw
        for fleem in updateable:
            fleem.update(dt)
        for bleem in drawable:
            bleem.draw(screen)
        for kleem in asteroids:
            if kleem.collision(player):
                sys.exit("Game over man!")
            for sleem in shots:
                if kleem.collision(sleem):
                    kleem.split()
                    sleem.kill()

        # update display
        pygame.display.flip()

        # limit frames to 60 FPS
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
