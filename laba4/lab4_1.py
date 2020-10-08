import pygame
from pygame.draw import *
pygame.init()
screen = pygame.display.set_mode((400, 400))

FPS = 30

circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (0, 0, 0), (130, 150), 18)
circle(screen, (0, 0, 0), (270, 150), 16)
circle(screen, (255, 0, 0), (130, 150), 20, 4)
circle(screen, (255, 0, 0), (270, 150), 18, 3)
rect(screen, (0, 0, 0), (130, 250, 140, 20))
line(screen, (0, 0, 0), [80, 110], [150, 130], 15)
line(screen, (0, 0, 0), [320, 110], [250, 130], 15)
pygame.display.update()


clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True