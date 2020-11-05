import pygame
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
win = 0  # равно 0, если поражение; дальше меняется на 1, если победа
k = 5  # количество жизней у особой мищени
max = 25  # максимальная скорость особой мишени
color = (10, 255, 18)  # первоначальный цвет особой мишени
score = 0  # счёт
game_time = 100 * 1000  # время игры
screen = pygame.display.set_mode((w, h))
font_name = pygame.font.match_font('arial')
clock = pygame.time.Clock()
finished = False
print('Введите количество шаров:')
number_of_balls = int(input())

def ball():
    """Функция рисует шарик случайного цвета, радиуса, со случайной скоростью в случайном месте.
    Усложнённая система рандома, чтобы скорость не обнулилась. Возвращает словарь"""
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
    """Функция рисует специальную мишень со случайными скоростью и ускорением в случайном месте.
    Усложнённая система рандома, чтобы скорость/ускорение не обнулились. Возвращает словарь"""
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


def col_target(list):
    """При столкновении спец. мишени со стенкой компонента скорости менеятся на противоположную, а сам шарик
    перемещается чуть выше (чтобы не забаговался)"""
    if list['x'] >= w - list['r']:
        list['vx'] = -list['vx']
        list['x'] -= list['r']
    if list['x'] <= list['r']:
        list['vx'] = -list['vx']
        list['x'] += list['r']
    if list['y'] >= h - list['r']:
        list['vy'] = -list['vy']
        list['y'] -= list['r']
    if list['y'] <= list['r']:
        list['vy'] = -list['vy']
        list['y'] += list['r']
    if target['vx'] >= max or target['vx'] <= -max:
        target['ax'] = -target['ax']  # Если скорость больше максимальной, то она меняет направление на противоположное
    if target['vy'] >= max or target['vy'] <= -max:
        target['ay'] = -target['ay']


def col_ball(list):
    """При столкновении обычного шарика со стенкой компонента скорости менеятся на противоположную"""
    if list['x'] >= w - list['r']:
        list['vx'] = -list['vx']
    if list['x'] <= list['r']:
        list['vx'] = -list['vx']
    if list['y'] >= h - list['r']:
        list['vy'] = -list['vy']
    if list['y'] <= list['r']:
        list['vy'] = -list['vy']


def move_ball(ball):
    """Функция описывает движение обычной мишени (отражение от стен, скорость, координаты)"""
    circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])
    x = ball['x'] + ball['vx']
    y = ball['y'] + ball['vy']
    ball['x'] = x
    ball['y'] = y
    col_ball(ball)


def move_target(target):
    """Функция описывает движение спец. мишени (отражение от стен, скорость, ускорение)"""
    circle(screen, color, (target['x'], target['y']), target['r'])
    x1 = target['x'] + target['vx']
    vx = target['vx'] + target['ax']
    y1 = target['y'] + target['vy']
    vy = target['vy'] + target['ay']
    target['x'] = x1
    target['y'] = y1
    target['vx'] = vx
    target['vy'] = vy
    col_target(target)


def target_life(k):
    """После попадания по цели её жизнь уменьшается, а цвет меняется. Возвращает цвет особой мишени"""
    if k == 5:
        color = (10, 255, 18)
    elif k == 4:
        color = (170, 255, 0)
    elif k == 3:
        color = (255, 255, 5)
    elif k == 2:
        color = (255, 179, 0)
    elif k == 1:
        color = (255, 17, 0)
    elif k == 0:
        color = (0, 0, 0)
        targets.remove(target)
    return color


def draw_text(surf, text, size, x, y):
    """Функция оставляет белую надпись заданного размера на заданных координатах"""
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


balls = [ball() for i in range(number_of_balls)]
targets = [special_target()]
while not finished:
    clock.tick(FPS)
    timer = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    if timer >= game_time:  # Таймер на game_time миллисекунд. Если не убрать все шары за это время, игра закончится
        for ball in balls:
            balls.remove(ball)
        for target in targets:
            targets.remove(target)
        draw_text(screen, "Game over", 200, w / 2, h / 2)
    for target in targets:
        move_target(target)
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = event.pos
            if (target['x'] - mx) ** 2 + (target['y'] - my) ** 2 <= target['r'] ** 2:
                score += 100  # очки за особую мишень
                k -= 1
                color = target_life(k)
    for ball in balls:
        move_ball(ball)
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = event.pos
            if (ball['x'] - mx) ** 2 + (ball['y'] - my) ** 2 <= ball['r'] ** 2:
                balls.remove(ball)
                score += 80 - ball['r']  # очки за обычную мишень
    draw_text(screen, "score: " + str(score), 80, w / 2, 10)
    if len(balls) == 0 and len(targets) == 0 and timer < game_time:  # Если все шары убраны, то победа
        win = 1
        draw_text(screen, "Congratulations!", 200, w / 2, h / 2)
    rect(screen, WHITE, (w / 4, h / 8, w / 2, h / 16))
    l = timer / game_time * (w / 2)
    if l <= w / 2:
        rect(screen, GREEN, (w / 4, h / 8, l, h / 16))
    pygame.display.update()
    screen.fill(BLACK)
if win == 1:  # Если победа, то игрок записывается в файл
    print("Введите Ваше имя:")
    name = str(input())
    records = open('records.txt', 'a')
    records.write(name + ' : ' + str(score) + '\n')
    records.close()
pygame.quit()