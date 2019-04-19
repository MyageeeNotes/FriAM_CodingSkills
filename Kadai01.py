# coding: utf-8
# Coding Skills: Kadai01
# 345(29) Daigo Miyajima

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

if __name__ == "__main__":
    player, enemy_max, enemies = initialize()
    start(player, enemy_max, enemies)
