import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((400, 550))
green = (18, 252, 1)
blue = (0, 250, 250)
yellow = (250, 250, 0)
gray = (233, 249, 245)
dark_green = (23, 152, 44)
pink = (255, 189, 189)
white = (255, 255, 255)
unicorn1 = (171, 225, 242)
unicorn2 = (246, 187, 236)
unicorn3 = (238, 245, 175)
light_green = (0, 255, 26)

rect(screen, blue, (0, 0, 400, 550 / 2))
circle(screen, (250, 250, 0), (380, 50), 70)
rect(screen, green, (0, 550 / 2, 400, 550 / 2))
FPS = 30

def tree(x, y, n):
    rect(screen, gray, (x - int(120 / n), y - int(37.5 / n), int(30 / n), int(100 / n)))
    ellipse(screen, dark_green, (x - int(180 / n), y - int(110 / n), int(155 / n), int(100 / n)))
    ellipse(screen, dark_green, (x - int(220 / n), y - int(180 / n), int(230 / n), int(120 / n)))
    ellipse(screen, dark_green, (x - int(170 / n), y - int(260 / n), int(140 / n), int(160 / n)))
    circle(screen, pink, (x - int(60 / n), y - int(210 / n)), int(17 / n))
    circle(screen, pink, (x - int(20 / n), y - int(120 / n)), int(17 / n))
    circle(screen, pink, (x - int(195 / n), y - int(115 / n)), int(17 / n))
    circle(screen, pink, (x - int(145 / n), y - int(40 / n)), int(17 / n))


def unicorn(x, y, n, znak):
    # единорог - тело, голова и ноги
    ellipse(screen, white, (x - int(160 / n) * int((1 - znak) / 2), y, int(160 / n), int(80 / n)))
    rect(screen, white, (x + znak * int(40 / n) - int(19 / n) * int((1 - znak) / 2), y + int(70 / n), int(19 / n), int(60 / n)))
    rect(screen, white, (x + znak * int(8 / n) - int(15 / n) * int((1 - znak) / 2), y + int(50 / n), int(15 / n), int(90 / n)))
    rect(screen, white, (x + znak * int(98 / n) - int(17 / n) * int((1 - znak) / 2), y + int(50 / n), int(17 / n), int(93 / n)))
    rect(screen, white, (x + znak * int(130 / n) - int(15 / n) * int((1 - znak) / 2), y + int(50 / n), int(15 / n), int(77 / n)))
    rect(screen, white, (x + znak * int(100 / n) - int(50 / n) * int((1 - znak) / 2), y - int(50 / n), int(50 / n), int(100 / n)))
    ellipse(screen, white, (x + znak * int(100 / n) - int(65 / n) * int((1 - znak) / 2), y - int(78 / n), int(65 / n), int(50 / n)))
    ellipse(screen, white, (x + znak * int(118 / n) - int(70 / n) * int((1 - znak) / 2), y - int(65 / n), int(70 / n), int(30 / n)))
    circle(screen, (229, 153, 206), (x + znak * int(138 / n) - int(8 / n) * int((1 - znak) / 2), y - int(60 / n)), int(8 / n))
    ellipse(screen, white, (x + znak * int(132 / n) - int(8 / n) * int((1 - znak) / 2), y - int(65 / n), int(8 / n), int(5 / n)))
    polygon(screen, pink, [[x + znak * int(120 / n), y - int(75 / n)], [x + znak * int(135 / n), y - int(145 / n)], [x + znak * int(138 / n), y - int(77 / n)]])
    # цвета - грива
    ellipse(screen, unicorn1, (x + znak * int(65 / n) - int(63 / n) * int((1 - znak) / 2), y - int(30 / n), int(63 / n), int(15 / n)))
    ellipse(screen, pink, (x + znak * int(70 / n) - int(50 / n) * int((1 - znak) / 2), y - int(80 / n), int(50 / n), int(18 / n)))
    ellipse(screen, unicorn2, (x + znak * int(67 / n) - int(53 / n) * int((1 - znak) / 2), y - int(65 / n), int(53 / n), int(25 / n)))
    ellipse(screen, unicorn1, (x + znak * int(65 / n) - int(60 / n) * int((1 - znak) / 2), y - int(50 / n), int(60 / n), int(14 / n)))
    ellipse(screen, pink, (x + znak * int(68 / n) - int(43 / n) * int((1 - znak) / 2), y - int(75 / n), int(43 / n), int(15 / n)))
    ellipse(screen, unicorn3, (x + znak * int(62 / n) - int(49 / n) * int((1 - znak) / 2), y - int(40 / n), int(49 / n), int(25 / n)))
    ellipse(screen, unicorn1, (x + znak * int(50 / n) - int(60 / n) * int((1 - znak) / 2), y - int(34 / n), int(60 / n), int(15 / n)))
    ellipse(screen, unicorn2, (x + znak * int(45 / n) - int(75 / n) * int((1 - znak) / 2), y - int(20 / n), int(75 / n), int(15 / n)))
    ellipse(screen, pink, (x + znak * int(30 / n) - int(75 / n) * int((1 - znak) / 2), y - int(10 / n), int(75 / n), int(13 / n)))
    ellipse(screen, unicorn1, (x + znak * int(13 / n) - int(55 / n) * int((1 - znak) / 2), y + int(5 / n), int(55 / n), int(15 / n)))
    ellipse(screen, unicorn2, (x - int(55 / n) * int((1 - znak) / 2), y - int(5 / n), int(55 / n), int(18 / n )))
    # цвета - хвост
    ellipse(screen, unicorn1, (x - znak * int(30 / n) - int(60 / n) * int((1 - znak) / 2), y + int(36 / n), int(60 / n), int(15 / n)))
    ellipse(screen, unicorn2, (x - znak * int(40 / n) -int(75 / n) * int((1 - znak) / 2), y + int(50 / n), int(75 / n), int(15 / n)))
    ellipse(screen, pink, (x -  znak *int(60 / n) - int(75 / n) * int((1 - znak) / 2), y + int(60 / n), int(75 / n), int(13 / n)))
    ellipse(screen, unicorn3, (x - znak * int(70 / n) - int(65 / n) * int((1 - znak) / 2), y + int(65 / n), int(65 / n), int(13 / n)))
    ellipse(screen, unicorn1, (x - znak * int(65 / n) - int(60 / n) * int((1 - znak) / 2), y + int(70 / n), int(60 / n), int(15 / n)))
    ellipse(screen, unicorn3, (x - znak * int(80 / n) - int(70 / n) * int((1 - znak) / 2), y + int(75 / n), int(70 / n), int(13 / n)))
    ellipse(screen, unicorn2, (x - znak * int(95 / n) - int(75 / n) * int((1 - znak) / 2), y + int(84 / n), int(75 / n), int(18 / n)))
    ellipse(screen, unicorn3, (x - znak * int(70 / n) - int(85 / n) * int((1 - znak) / 2), y + int(94 / n), int(85 / n), int(13 / n)))
    ellipse(screen, unicorn1, (x - znak * int(65 / n) - int(80 / n) * int((1 - znak) / 2), y + int(104 / n), int(80 / n), int(17 / n)))
    ellipse(screen, unicorn3, (x - znak * int(60 / n) - int(80 / n) * int((1 - znak) / 2), y + int(114 / n), int(80 / n), int(19 / n)))
    ellipse(screen, unicorn2, (x - znak * int(50 / n) - int(85 / n) * int((1 - znak) / 2), y + int(115 / n), int(85 / n), int(18 / n)))


unicorn(165, 355, 1, 1)
tree(200, 340, 1)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True