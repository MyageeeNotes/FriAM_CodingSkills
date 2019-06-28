# coding: utf-8
# Coding Skills: Kadai01
# 345(29)


# データ読み込み
# IN:
#   -str(改行区切りデータ)
# OUT:
#   -[int(p)] = 自機データ,
#   -int(e_max) = 敵機数,
#   -[int(enms)] = 敵機データ
def initialize(d):

    data_list = d.split('\n')   # 改行区切り

    # 自機データ
    p = data_list.pop(0).split(' ') # スペース区切り
    p = [int(s) for s in p]     # 整数型に変換

    # 敵機データ
    e_max = int(data_list.pop(0))
    enms = []
    for x in range(e_max):
        data = data_list[x].split(' ')
        data = [int(s) for s in data]
        enms.append(data)

    return p, e_max, enms


def judge(player, enemy_max, enemies):
    for i in range(enemy_max):

        px, py, pw, ph = player
        ex, ey, ew, eh = enemies[i]

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
                print('敵機 {} が当たり'.format(i + 1))
