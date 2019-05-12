# coding: utf-8
# Coding Skills: Kadai02-5
# 345(29) Daigo Miyajima

# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
from FriAM_CodingSkills import Kadai02 as Poker
screen = None
se = None


def play_screen(scr):
    while True:
        scr.fill((0, 0, 0))        # 画面を黒色(#000000)に塗りつぶし
        scr.blit(bgImage_play, (0, 0))
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
