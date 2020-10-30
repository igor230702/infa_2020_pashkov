from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))
w = 800
h = 600
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.a = 1
        self.time = 100
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def collision(self):
        if self.x >= w - self.r:
            self.vx = -self.vx
            self.x -= self.r
        if self.x <= self.r:
            self.vx = -self.vx
            self.x += self.r
        if self.y >= h - self.r:
            self.vy = -self.vy
            self.y -= self.r
        if self.y <= self.r:
            self.vy = -self.vy
            self.y += self.r


    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        vy = self.vy + self.a
        self.vy = vy
        x = self.x + self.vx
        y = self.y + self.vy
        self.set_coords()
        self.x = x
        self.y = y
        self.collision()


    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)  # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        if event.x-new_ball.x != 0:
            self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event and event.x - 20 != 0:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
        )
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        r = self.r = rnd(2, 50)
        x = self.x = rnd(600 + r, 780 - r)
        y = self.y = rnd(300 + r, 550 - r)
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def collision(self):
        if self.x >= w - self.r:
            self.vx = -self.vx
        if self.x <= self.r:
            self.vx = -self.vx
        if self.y >= h - self.r:
            self.vy = -self.vy
        if self.y <= self.r:
            self.vy = -self.vy

    def move(self):
        x = self.x + self.vx
        y = self.y + self.vy
        self.set_coords()
        self.x = x
        self.y = y
        self.collision()

    def hit(self, points=1):
        self.x = -100
        self.y = -100
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
screen2 = canv.create_text(400, 400, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, t2, screen1, screen2, balls, bullet
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = t2.live = 1
    while t1.live or t2.live or balls:
        t1.move()
        t2.move()
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live -= 1
                t1.hit()
                canv.itemconfig(screen1, text='Вы уничтожили цель 1 за ' + str(bullet) + ' выстрелов')
            if b.hittest(t2) and t2.live:
                t2.live -= 1
                t2.hit()
                canv.itemconfig(screen2, text='Вы уничтожили цель 2 за ' + str(bullet) + ' выстрелов')
            b.time -= 1
            if b.time == 0:
                canv.delete(b.id)
                balls.remove(b)
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.itemconfig(screen2, text='')
    canv.delete(gun)
    root.after(2 * 1000, new_game)


new_game()


root.mainloop()