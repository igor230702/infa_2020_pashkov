import pygame
import math as m
from pygame.draw import *
from random import randint

pygame.init()
FPS = 60
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, MAGENTA, CYAN]
w = 1200
h = 800
screen = pygame.display.set_mode((w, h))


def ball():
    """Функция рисует шарик случайного цвета, радиуса, со случайной скоростью и в случайном месте. Возвращает словарь"""
    x0 = randint(100, 1100)
    y0 = randint(100, 700)
    if randint(0, 1) == 0:
        vx = randint(-6, -2)
    else:
        vx = randint(2, 6)
    if randint(0, 1) == 0:
        vy = randint(-6, -2)
    else:
        vy = randint(2, 6)
    r = randint(30, 60)
    color = COLORS[randint(0, 4)]
    circle(screen, color, (x0, y0), r)
    ball = {
        'x': x0,
        'y': y0,
        'vx': vx,
        'vy': vy,
        'r': r,
        'color': color
    }
    return ball


def special_target():
    """Функция рисует специальную мишень со случайными скоростью и ускорением и в случайном месте. Возвращает словарь"""
    x0 = randint(100, 1100)
    y0 = randint(100, 700)
    if randint(0, 1) == 0:
        vx = randint(-4, -1)
        ax = randint(-3, -1)
    else:
        vx = randint(1, 4)
        ax = randint(1, 3)
    if randint(0, 1) == 0:
        vy = randint(-4, -1)
        ay = randint(-3, -1)
    else:
        vy = randint(1, 4)
        ay = randint(1, 3)
    r = 40
    color = (255, 255, 255)
    circle(screen, (255, 255, 255), (x0, y0), r)
    target = {
        'x': x0,
        'y': y0,
        'vx': vx,
        'vy': vy,
        'ax': ax,
        'ay': ay,
        'r': r,
        'color': color
    }
    return target


font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    """Функция оставляет белую надпись заданного размера на заданных координатах"""
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def move_ball(ball):


balls = [ball(), ball(), ball(), ball(), ball(), ball(), ball(), ball(), ball(), ball(), ball(), ball(), ball(), ball(),
         ball(), ball(), ball(), ball(), ball(), ball()]
targets = [special_target()]
clock = pygame.time.Clock()
finished = False
win = 0  # 0, если поражение; дальше меняется на 1, если победа
k = 5  # количество жизней у особой мищени
max = 25  # максимальная скорость особой мишени
color = (10, 255, 18)  # цвет особой мишени
score = 0
print("Введите Ваше имя")
name = str(input())
while not finished:
    clock.tick(FPS)
    timer = pygame.time.get_ticks()
    if timer >= 120 * 1000:  # Таймер на две минуты. Если не убрать все шары за это время, игра закончится
        for ball in balls:
            balls.remove(ball)
        for target in targets:
            targets.remove(target)
        draw_text(screen, "Game over", 200, w / 2, h / 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    for target in targets:
        circle(screen, color, (target['x'], target['y']), target['r'])
        x1 = target['x'] + target['vx']
        vx = target['vx'] + target['ax']
        y1 = target['y'] + target['vy']
        vy = target['vy'] + target['ay']
        target['x'] = x1
        target['y'] = y1
        target['vx'] = vx
        target['vy'] = vy
        if target['vx'] >= max or target['vx'] <= -max:
            target['ax'] = -target[
                'ax']  # Если скорость больше максимальной, то она меняет направление на противоположное
        if target['vy'] >= max or target['vy'] <= -max:
            target['ay'] = -target['ay']
        if target['x'] >= 1200 - target['r']:
            target['vx'] = -target['vx']
            target['x'] = target['x'] - target['r']
        if target['x'] <= target['r']:
            target['vx'] = -target['vx']
            target['x'] = target['x'] + target['r']
        if target['y'] >= 800 - target['r']:
            target['vy'] = -target['vy']
            target['y'] = target['y'] - target['r']
        if target['y'] <= target['r']:
            target['vy'] = -target['vy']
            target['vy'] = target['y'] + target['r']
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = event.pos
            if (target['x'] - mx) ** 2 + (target['y'] - my) ** 2 <= target['r'] ** 2:
                score += 100  # 100 очков за попадание по особой мишени
                k -= 1
                if k == 5:
                    color = (10, 255, 18)  # После попадания по особой мишени её цвет меняется
                elif k == 4:
                    color = (170, 255, 0)
                elif k == 3:
                    color = (255, 255, 5)
                elif k == 2:
                    color = (255, 179, 0)
                elif k == 1:
                    color = (255, 17, 0)
                elif k == 0:
                    targets.remove(target)
    for ball in balls:
        circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])
        x = ball['x'] + ball['vx']
        y = ball['y'] + ball['vy']
        ball['x'] = x
        ball['y'] = y
        if ball['x'] >= 1200 - ball['r'] or ball['x'] <= ball['r']:
            ball['vx'] = -ball['vx']
        if ball['y'] >= 800 - ball['r'] or ball['y'] <= ball['r']:
            ball['vy'] = -ball['vy']
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = event.pos
            if (ball['x'] - mx) ** 2 + (ball['y'] - my) ** 2 <= ball['r'] ** 2:
                balls.remove(ball)
                score += 80 - ball['r']  # 80 - (радиус шарика) очков за обычную мишень
    draw_text(screen, "score: " + str(score), 80, w / 2, 10)
    if len(balls) == 0 and len(targets) == 0 and timer < 120 * 1000:
        win = 1
        draw_text(screen, "Congratulations!", 200, w / 2, h / 2)  # Если все шары убраны, игра заканчивается
    pygame.display.update()
    screen.fill(BLACK)
if win == 1:
    records = open('records.txt', 'a')
    records.write(name + ' : ' + str(score) + '\n')
    records.close()
pygame.quit()