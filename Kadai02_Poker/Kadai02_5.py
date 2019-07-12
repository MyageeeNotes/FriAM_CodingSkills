# coding: utf-8
# Coding Skills: Kadai02-5
# 345(30)

import pygame
from pygame.locals import *
import sys
import os
import time
import Kadai02 as Poker


# ------------------------------
# Dealing cards information.
# CPU data and YOUR data
# ------------------------------
class Table:
    # Initialize
    def __init__(self, scr):
        self.screen = scr
        
        # Cards data class
        self.you = []
        self.cpu = []

        # [suit, number] x5
        self.your_data = []
        self.cpu_data = []
        
        # Hand name image
        self.name_image = {'you': '', 'cpu': ''}
        
        # Finish dealing cards for animation
        self.you_deal = 0
        self.cpu_deal = 0

    def load_nm_img(self, turn, pt):
        p = os.path.join('Name', str(pt) + '.png')
        if turn == 0:
            self.name_image['you'] = pygame.image.load(p)
            self.name_image['you'] = pygame.transform.scale(
                self.name_image['you'], (1500, 500))
        else:
            self.name_image['cpu'] = pygame.image.load(p)
            self.name_image['cpu'] = pygame.transform.scale(
                self.name_image['cpu'], (900, 300))

    def display_nm_img(self):
        self.screen.blit(self.name_image['cpu'], (200, 5))
        self.screen.blit(self.name_image['you'], (-80, 180))

    def dealing(self, turn, pos):
        if turn == 0:
            dt = self.you[pos]
        else:
            dt = self.cpu[pos]

        dt.display()

        you_deal = 0
        cpu_deal = 0
        for i in range(5):
            if self.you[i].pos_set:
                you_deal += 1
            if self.cpu[i].pos_set:
                cpu_deal += 1

        self.you_deal = you_deal
        self.cpu_deal = cpu_deal

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
        self.bg_img = os.path.join('Cards', 'zbk.png')
        self.bg_img = pygame.image.load(self.bg_img)
        self.screen = scr

        # SET: Image file
        if self.turn == 0:
            self.scale = 0.25
        else:
            self.scale = 0.15

        s = ['c', 'd', 'h', 's', 'j']
        file_name = s[self.suit] + str(self.num) + '.png'
        file_path = os.path.join('Cards', file_name)
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


def card_all_reset(tb, scr, cpk, jf):
    # Create YOUR data -----
    se_deals5.play()
    your_data = Poker.initialize(cpk)
    your_name = Poker.judge(your_data)
    your_point = Poker.battle(your_name)
    for cnt in range(len(your_data)):
        tb.you[cnt] = Card(0, scr, your_data[cnt], cnt)

    if len(cpk.cards) < 5:
        package = Poker.CardPack(jf)

        for i in range(5):
            yd = tb.you[i]
            cd = tb.cpu[i]
            package.cards.remove([yd.suit, yd.num])
            package.cards.remove([cd.suit, cd.num])

        return your_point, package

    return your_point, cpk


def card_reset(pos, tb, scr, cpk, jf):
    # Create YOUR data -----
    se_deals1.play()
    tb.your_data[pos] = Poker.draw_card(cpk)
    your_name = Poker.judge(tb.your_data)
    your_point = Poker.battle(your_name)
    tb.you[pos] = Card(0, scr, tb.your_data[pos], pos)
    tb.you[pos].flip = True

    if len(cpk.cards) < 5:
        package = Poker.CardPack(jf)

        for i in range(5):
            yd = tb.you[i]
            cd = tb.cpu[i]
            package.cards.remove([yd.suit, yd.num])
            package.cards.remove([cd.suit, cd.num])

        return your_point, package

    return your_point, cpk


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
        pygame.mixer.music.load("./sound/255-Invitation.mp3")
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.load("./sound/256-Fail.mp3")
        pygame.mixer.music.play(-1)
    time.sleep(1)

    cnt = 0
    while True:
        pygame.display.update()
        cnt += 1
        if cnt == 14000:
            pygame.mixer.music.fadeout(1000)
            title_screen(scr)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    se.play()
                    pygame.mixer.music.fadeout(1000)
                    title_screen(scr)


def play_screen(scr):
    scr.fill((0, 0, 0))
    table = Table(scr)
    time.sleep(1)
    pygame.mixer.music.load("./sound/Poker_battle_bgm.mp3")
    pygame.mixer.music.play(-1)

    # Create CPU data -----
    joker_flag = True
    card_pack = Poker.CardPack(joker_flag)

    table.cpu_data = Poker.initialize(card_pack)
    cpu_name = Poker.judge(table.cpu_data)
    cpu_point = Poker.battle(cpu_name)
    for cnt in range(len(table.cpu_data)):
        card = Card(1, scr, table.cpu_data[cnt], cnt)
        table.cpu.append(card)

    # Create YOUR data -----
    table.your_data = Poker.initialize(card_pack)
    your_name = Poker.judge(table.your_data)
    your_point = Poker.battle(your_name)
    for cnt in range(len(table.your_data)):
        card = Card(0, scr, table.your_data[cnt], cnt)
        table.you.append(card)

    se_deals5.play()
    key_list = [K_1, K_2, K_3, K_4, K_5]
    while True:
        scr.blit(bgImage_play2, (0, 0))
        for i in range(5):
            table.dealing(1, i)
            table.dealing(0, i)
        pygame.display.update()

        # Event
        for event in pygame.event.get():
            # Close window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Keyboard event
            if event.type == KEYDOWN:

                if event.key == K_SPACE:
                    se.play()
                    your_point, card_pack = card_all_reset(table, screen, card_pack, joker_flag)

                if event.key == K_RETURN:
                    if table.you_deal == 5:
                        se.play()
                        card_set(table, screen, your_point, cpu_point)

                if event.key in key_list:
                    for i in range(len(key_list)):
                        if event.key == key_list[i]:
                            your_point, card_pack = card_reset(i, table, screen, card_pack, joker_flag)


def title_screen(scr):
    # play Title BGM
    pygame.mixer.music.load("./sound/249_NightCity.mp3")
    pygame.mixer.music.play(-1)

    while True:
        # Renew background image
        scr.fill((0, 0, 0))
        scr.blit(bgImage, (0, 0))
        pygame.display.update()

        # Events
        for event in pygame.event.get():

            # Close window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Keyboard event
            if event.type == KEYDOWN:
                pygame.mixer.music.stop()
                se.play()
                play_screen(scr)


if __name__ == "__main__":

    # SET UP -----
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("POKER - Kadai0205")

    path = './image/'
    bgImage = pygame.image.load(path + "title.png")
    bgImage_play = pygame.image.load(path + "play.png")
    bgImage_play2 = pygame.image.load(path + "play3.png")

    path = './sound/'
    se = pygame.mixer.Sound(path + "decision3.wav")
    se_deals1 = pygame.mixer.Sound(path + "deal1.wav")
    se_deals5 = pygame.mixer.Sound(path + "deal5.wav")

    # MAIN LOOP -----
    title_screen(screen)
