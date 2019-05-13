# coding: utf-8
# Coding Skills: Kadai02-5
# 345(29) Daigo Miyajima

# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import os
import time
from FriAM_CodingSkills import Kadai02 as Poker
screen = None
se = None


class Table:
    def __init__(self, scr):
        self.you = []
        self.cpu = []
        self.screen = scr
        self.you_nm_img = ''
        self.cpu_nm_img = ''

    def load_nm_img(self, turn, pt):
        if turn == 0:
            path = os.path.join('Kadai02', 'Name', str(pt) + '.png')
            self.you_nm_img = pygame.image.load(path)
            self.you_nm_img = pygame.transform.scale(
                self.you_nm_img, (1500, 500))
        else:
            path = os.path.join('Kadai02', 'Name', str(pt) + '.png')
            self.cpu_nm_img = pygame.image.load(path)
            self.cpu_nm_img = pygame.transform.scale(
                self.cpu_nm_img, (900, 300))

    def display_nm_img(self):
        self.screen.blit(self.cpu_nm_img, (200, 5))
        self.screen.blit(self.you_nm_img, (-80, 180))

    def dealing(self, turn, pos):
        if turn == 0:
            dt = self.you[pos]
        else:
            dt = self.cpu[pos]

        dt.display()

        self.you_deal = 0
        self.cpu_deal = 0
        for i in range(5):
            if self.you[i].pos_set:
                self.you_deal += 1
            if self.cpu[i].pos_set:
                self.cpu_deal += 1

        if self.you_deal == 5:
            if self.cpu_deal == 5:
                if not self.you[4].flip:
                    for i in range(5):
                        if not self.you[i].flip:
                            self.you[i].flip = True


class Card:
    def __init__(self, trn, scr, dt, c):
        self.turn = trn
        self.suit = dt[0]
        self.num = dt[1]
        self.pos = [0, 0]
        self.pos_now = [0, 0]
        self.pos_head = [0, 0]
        self.pos_num = c
        self.pos_set = False
        self.flip = False
        self.size = [768, 1024]
        self.scale = 1
        self.bg_img = os.path.join('Kadai02', 'Cards', 'zbk.png')
        self.bg_img = pygame.image.load(self.bg_img)
        self.screen = scr

        # SET: Image file
        if self.turn == 0:
            self.scale = 0.25
        else:
            self.scale = 0.15

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
        if self.turn == 0:
            self.pos_head = [120, 300]
            self.pos_now = [0, 300]
        else:
            self.pos_head = [320, 80]
            self.pos_now = [0, 80]

        margin = 20
        img_width = int(self.size[0] * self.scale)
        self.pos[0] = img_width * c + margin * c
        self.pos[0] += self.pos_head[0]
        self.pos[1] = self.pos_head[1]

    def deal_animation(self):
        if abs(self.pos_now[0] - self.pos[0]) > 20:
            speed = 40
        else:
            speed = 1

        if self.pos_now[0] < self.pos[0]:
            self.pos_now[0] += speed
        elif self.pos_now[0] > self.pos[0]:
            self.pos_now[0] -= speed
        else:
            self.pos_set = True

        if self.pos_now[1] < self.pos[1]:
            self.pos_now[1] += speed
        elif self.pos_now[1] > self.pos[1]:
            self.pos_now[1] -= speed

    def display(self):
        if self.flip:
            self.deal_animation()
            self.screen.blit(self.img, self.pos_now)
            
        else:
            self.deal_animation()
            self.screen.blit(self.bg_img, self.pos_now)


def card_reset(tb, scr):
    # Create YOUR data -----
    se_deals.play()
    your_data, joker_flag = Poker.initialize(True)
    your_name = Poker.judge(your_data)
    your_point = Poker.battle(your_name)
    for cnt in range(len(your_data)):
        tb.you[cnt] = Card(0, scr, your_data[cnt], cnt)

    return your_point


def card_set(tb, scr, yp, cp):
    pygame.mixer.music.fadeout(1000)
    scr.blit(bgImage_play, (0, 0))
    for j in range(5):
        tb.cpu[j].flip = True
        tb.dealing(1, j)
        tb.dealing(0, j)
    pygame.display.update()
    time.sleep(0.5)

    tb.load_nm_img(0, yp)
    tb.load_nm_img(1, cp)
    tb.display_nm_img()
    if yp > cp:
        pygame.mixer.music.load("./Kadai02/255-Invitation.mp3")
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.load("./Kadai02/256-Fail.mp3")
        pygame.mixer.music.play(-1)
    time.sleep(1)

    cnt = 0
    while True:
        pygame.display.update()
        cnt += 1
        if cnt == 15000:
            pygame.mixer.music.fadeout(1000)
            title_screen()
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    se.play()
                    pygame.mixer.music.fadeout(1000)
                    title_screen()


def play_screen(scr):
    scr.fill((0, 0, 0))  # 画面を黒色(#000000)に塗りつぶし
    table = Table(scr)
    time.sleep(1)
    pygame.mixer.music.load("./Kadai02/254-Through.mp3")
    pygame.mixer.music.play(-1)

    # Create CPU data -----
    joker_flag = True
    cpu_data, joker_flag = Poker.initialize(joker_flag)
    cpu_name = Poker.judge(cpu_data)
    cpu_point = Poker.battle(cpu_name)
    for cnt in range(len(cpu_data)):
        card = Card(1, scr, cpu_data[cnt], cnt)
        table.cpu.append(card)

    # Create YOUR data -----
    your_data, joker_flag = Poker.initialize(joker_flag)
    your_name = Poker.judge(your_data)
    your_point = Poker.battle(your_name)
    for cnt in range(len(your_data)):
        card = Card(0, scr, your_data[cnt], cnt)
        table.you.append(card)

    se_deals.play()
    while True:
        scr.blit(bgImage_play2, (0, 0))
        for i in range(5):
            table.dealing(1, i)
            table.dealing(0, i)
        pygame.display.update()     # 画面を更新

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    se.play()
                    your_point = card_reset(table, screen)
                if event.key == K_RETURN:
                    se.play()
                    card_set(table, screen, your_point, cpu_point)


def title_screen():
    pygame.mixer.music.load("./Kadai02/249_NightCity.mp3")
    pygame.mixer.music.play(-1)
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
                pygame.mixer.music.stop()
                se.play()
                play_screen(screen)


if __name__ == "__main__":

    # SET UP -----
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("POKER - Kadai0205")

    bgImage = pygame.image.load("./Kadai02/title.png")
    bgImage_play = pygame.image.load("./Kadai02/play.png")
    bgImage_play2 = pygame.image.load("./Kadai02/play2.png")

    se = pygame.mixer.Sound("./Kadai02/decision3.wav")
    se_deals = pygame.mixer.Sound("./Kadai02/deal5.wav")

    # MAIN LOOP -----
    title_screen()
