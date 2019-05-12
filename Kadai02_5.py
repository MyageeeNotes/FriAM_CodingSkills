# coding: utf-8
# Coding Skills: Kadai02-5
# 345(29) Daigo Miyajima

# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import os
from FriAM_CodingSkills import Kadai02 as Poker
screen = None
se = None


class Table:
    def __init__(self, scr):
        self.you = []
        self.cpu = []
        self.screen = scr

    def dealing(self, turn, pos):
        if turn == 0:
            dt = self.you[pos]
        else:
            dt = self.cpu[pos]

        dt.display()


class Card:
    def __init__(self, scr, dt, c):
        self.suit = dt[0]
        self.num = dt[1]
        self.pos = [0, 0]
        self.pos_head = [320, 80]
        self.pos_num = c
        self.flip = False
        self.size = [768, 1024]
        self.scale = 0.15
        self.bg_img = os.path.join('Kadai02', 'Cards', 'zbk.png')
        self.bg_img = pygame.image.load(self.bg_img)
        self.screen = scr

        # SET: Image file
        s = ['c', 'd', 'h', 's', 'j']
        file_name = s[self.suit] + str(self.num) + '.png'
        file_path = os.path.join('Kadai02', 'Cards', file_name)
        self.img = pygame.image.load(file_path)
        self.img = pygame.transform.scale(
            self.img,
            (
                int(self.size[0] * self.scale),
                int(self.size[1] * self.scale)
            )
        )
        self.bg_img = pygame.transform.scale(
            self.bg_img,
            (
                int(self.size[0] * self.scale),
                int(self.size[1] * self.scale)
            )
        )

        # SET: Position
        margin = 20
        img_width = int(self.size[0] * self.scale)
        self.pos[0] = img_width * c + margin * c
        self.pos[0] += self.pos_head[0]
        self.pos[1] = self.pos_head[1]

    def display(self):
        if self.flip:
            self.screen.blit(self.img, self.pos)
        else:
            self.screen.blit(self.bg_img, self.pos)


def play_screen(scr):
    scr.fill((0, 0, 0))  # 画面を黒色(#000000)に塗りつぶし
    table = Table(scr)

    # Create CPU data -----
    joker_flag = True
    cpu_data, joker_flag = Poker.initialize(joker_flag)
    cpu_name = Poker.judge(cpu_data)
    cpu_point = Poker.battle(cpu_name)
    for cnt in range(len(cpu_data)):
        card = Card(scr, cpu_data[cnt], cnt)
        table.cpu.append(card)

    # Create YOUR data -----
    your_data, joker_flag = Poker.initialize(joker_flag)
    your_name = Poker.judge(your_data)
    your_point = Poker.battle(your_name)
    for cnt in range(len(cpu_data)):
        card = Card(scr, cpu_data[cnt], cnt)
        table.you.append(card)

    while True:
        scr.blit(bgImage_play, (0, 0))
        for i in range(5):
            table.dealing(1, i)
        pygame.display.update()     # 画面を更新

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()


def title_screen():
    while True:
        screen.fill((0, 0, 0))        # 画面を黒色(#000000)に塗りつぶし
        screen.blit(bgImage, (0, 0))
        pygame.display.update()     # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()
            if event.type == KEYDOWN:
                se.play()
                play_screen(screen)


if __name__ == "__main__":

    # SET UP -----
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("POKER - Kadai0205")

    bgImage = pygame.image.load("./Kadai02/title.png")
    bgImage_play = pygame.image.load("./Kadai02/play.png")

    pygame.mixer.music.load("./Kadai02/249_NightCity.mp3")
    pygame.mixer.music.play(-1)

    se = pygame.mixer.Sound("./Kadai02/hit_a.wav")

    # MAIN LOOP -----
    title_screen()
