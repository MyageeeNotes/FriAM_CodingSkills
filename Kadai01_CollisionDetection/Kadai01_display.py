# coding: utf-8
# Coding Skills: Kadai01
# 345(29) Daigo Miyajima

import sys
import tkinter

# Input Data
path = 'Kadai01_data.txt'

def initialize():
    with open(path) as f:

        player = f.readline().split(' ')
        player = [int(s) for s in player]

        enemy_max = int(f.readline())

        enemies = []
        for i in range(enemy_max):
            data = f.readline().split(' ')
            data = [int(s) for s in data]
            enemies.append(data)

    return player, enemy_max, enemies

def start(player,enemy_max,enemies):
    for i in range(enemy_max):
        px,py,pw,ph = player
        ex,ey,ew,eh = enemies[i]

        center = {
            'px': px + pw / 2, 'py': py + ph / 2,
            'ex': ex + ew / 2, 'ey': ey + eh / 2
        }

        distance = {
            'x': pw / 2 + ew / 2,
            'y': ph / 2 + eh / 2
        }

        if abs(center['px'] - center['ex']) < distance['x']:
            if abs(center['py'] - center['ey']) < distance['y']:
                print('敵機 {} が当たり'.format( i + 1 ))

def display(player, enemy_max, enemies):
    #
    # GUI設定
    #
    root = tkinter.Tk()
    root.title(u"Canvas")
    root.geometry("600x600")

    player = [x * 2 for x in player]
    #キャンバスエリア
    canvas = tkinter.Canvas(root, width = 600, height = 600)#Canvasの作成
    canvas.create_rectangle(
        player[0],
        player[1],
        player[2] + player[0],
        player[3] + player[1], fill = '#0090ff'
    )
    for i in range(enemy_max):
        canvas.create_rectangle(
            enemies[i][0],
            enemies[i][1],
            enemies[i][2] + enemies[i][0],
            enemies[i][3] + enemies[i][1], fill = '#ff9000'
        )

    #キャンバスバインド
    canvas.place(x=0, y=0)#Canvasの配置


    #
    # GUIの末端
    #
    root.mainloop()

if __name__ == "__main__":
    player, enemy_max, enemies = initialize()
    start(player, enemy_max, enemies)
    display(player, enemy_max, enemies)
