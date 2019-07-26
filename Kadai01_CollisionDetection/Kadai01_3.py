# coding: utf-8
# Coding Skills: Kadai01-3
# 課題１－３（オプション）

# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import time
import random

level = 0
rects = []
p = None
target_pos = [0, 0]


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.pos = [240, 740]
        self.size = 25
        self.color = (0, 127, 255)
        self.life = 5
        self.target = [0, 0]
        self.bullets = []

        self.display()

    def display(self):
        pygame.draw.ellipse(
            self.screen,
            self.color,
            (
                self.pos[0], self.pos[1],
                self.size, self.size
            )
        )

    def launch(self, head_bullet):
        y_speed = self.target[1]-self.pos[1]
        x_speed = self.target[0]-self.pos[0]
        vector = [y_speed / x_speed]

        if y_speed < 0:
            y_speed = -1
        elif y_speed > 0:
            y_speed = 1
        else:
            y_speed = 0

        if x_speed < 0:
            x_speed = -1
        elif x_speed > 0:
            x_speed = 1
        else:
            x_speed = 0

        vector.append(y_speed)
        vector.append(x_speed)

        shape = [self.screen, self.size, self.color]
        blt = Bullet(
            shape,
            vector,
            self.pos,
            head_bullet
        )
        self.bullets.append(blt)


class Bullet:
    def __init__(self, shape, vector, pos, head_bullet):
        self.screen = shape[0]
        self.size = shape[1]
        self.color = shape[2]
        self.pos = pos
        self.vector = vector
        self.head = head_bullet

    def update(self):
        speed, x, y = self.vector

        if x == 1:
            self.pos[0] += 1
            if self.pos[0] == 555:
                self.vector[1] = -1
        elif x == -1:
            self.pos[0] -= 1
            if self.pos[0] == 0:
                self.vector[1] = 1
        else:
            self.pos[0] -= 1
            if self.pos[0] == 0:
                self.vector[1] = 1

        if y == 1:
            self.pos[1] += speed
            if self.pos[1] == 780:
                self.vector[1] = -1
        else:
            self.pos[1] -= speed

    def display(self):
        pygame.draw.ellipse(
            self.screen,
            self.color,
            (
                self.pos[0], self.pos[1],
                self.size, self.size
            )
        )


class Block:
    def __init__(self, screen, axis, life):
        self.screen = screen
        self.size = 50
        self.color = (80, 80, 80)
        self.margin = 5
        self.pos = [
            (self.size + self.margin) * axis[0] + self.margin,
            (self.size + self.margin) * axis[1] + self.margin
        ]
        self.life = life

    def step(self):
        self.pos[1] += (self.size + self.margin)
        self.create()

    def create(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            Rect(
                self.pos[0], self.pos[1],
                self.size, self.size
            )
        )

        # フォントの作成
        sys_font = pygame.font.SysFont(None, 30)
        # テキストを描画したSurfaceを作成
        life = sys_font.render(str(self.life), True, (255, 255, 255))
        char_len = len(str(self.life))
        self.screen.blit(
            life,
            (
                self.pos[0] + (self.size / 2 - char_len * 6),
                self.pos[1] + 18
            )
        )


def line_update(screen):
    global level
    # Level UP
    level += 1

    # Step down the front line
    for blk in rects:
        blk.step()

    # Create Rect -----
    if level < 30:
        block_num = int(level / 10) + 1
        life = random.randint(1, level + 5)
    elif level >= 30 & level < 100:
        block_num = random.randint(3, 10)
        if block_num < 5:
            life = random.randint(80, 150)
        else:
            life = random.randint(5, 60)
    else:
        block_num = random.randint(8, 10)
        life = random.randint(50, 100 + level/2)

    # Decide block x pos
    line_max_list = list(range(10))
    blk_positions = []
    for i in range(int(block_num)):
        x = random.randint(0, len(line_max_list) - 1)
        blk_positions.append(line_max_list.pop(x))

    for i in range(int(block_num)):
        r = Block(screen, [blk_positions[i], 0], life)
        r.create()
        rects.append(r)


def target_line(play):
    pygame.draw.line(
        play.screen,
        (255, 255, 255),
        play.target,
        (play.pos[0]+12, play.pos[1]+12)
    )


def display(pl):
    # Blocks
    for blk in rects:
        blk.create()
    # player
    pl.display()
    # targetLine
    if pl.target != [0, 0]:
        target_line(pl)


def play(pl):
    cnt = 0
    pl.target = [0, 0]
    while cnt < 20:
        pl.screen.fill((0, 0, 0))
        time.sleep(0.01)
        display(pl)
        if cnt <= pl.life:
            if cnt == 0:
                pl.launch(1)
            else:
                pl.launch(0)

        for i in range(len(pl.bullets)):
            pl.bullets[i].update()
            pl.bullets[i].display()
        cnt += 1
        pygame.display.update()
    line_update(pl.screen)

def main():
    # SET UP -----
    pygame.init()
    screen = pygame.display.set_mode((555, 780))
    pygame.display.set_caption("Ban Dori - Kadai0103")

    screen.fill((0, 0, 0))
    line_update(screen)
    pl = Player(screen)

    before_time = time.time()
    duration = 0

    # MAIN LOOP -----
    while True:
        # FPS: 30
        now_time = time.time()
        duration = now_time - before_time
        delta_time = duration - (1/30)
        if delta_time > 0:
            time.sleep(delta_time)
        before_time = now_time

        screen.fill((0, 0, 0))
        display(pl)
        pygame.display.update()
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                #line_update(screen)
                play(pl)
                print(len(pl.bullets))
            if event.type == MOUSEBUTTONDOWN:
                pl.target = event.pos


if __name__ == "__main__":
    main()
