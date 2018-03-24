import pygame
from pygame.locals import *
import sys

pygame.init()


size = (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
image = pygame.image.load("ball.png")
rect = image.get_rect()
speed = [5, 5]
color = (0, 0, 0)


def update():
    rect.move_ip(speed)



def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        update()
        screen.fill(color)
        screen.blit(image, rect)
        pygame.display.flip()


if __name__ == "__main___":
    main()