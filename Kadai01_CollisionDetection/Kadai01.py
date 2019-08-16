# coding: utf-8
# Coding Skills: Kadai01

from PIL import Image


# データ読み込み
# IN:
#   -str(d:改行区切りデータ)
# OUT:
#   -[int(p)] = 自機データ,
#   -int(e_max) = 敵機数,
#   -[int(enms)] = 敵機データ
def initialize(d):

    data_list = d.split('\n')   # 改行区切り

    # 自機データ
    p = data_list.pop(0).split(' ')  # スペース区切り
    p = [int(s) for s in p]     # 整数型に変換

    # 敵機データ
    e_max = int(data_list.pop(0))
    enms = []
    for x in range(e_max):
        data = data_list[x].split(' ')
        data = [int(s) for s in data]
        enms.append(data)

    return p, e_max, enms


# 位置取得
# IN:
#   -p: 自機データ
#   -e: ターゲット敵機データ
# OUT:
#   - center: 各機の中央座標
#   - distance: 矩形での非接触ボーダー
def calc_location(p, e):
    px, py, pw, ph = p
    ex, ey, ew, eh = e

    center = {
        'px': px + pw / 2, 'py': py + ph / 2,
        'ex': ex + ew / 2, 'ey': ey + eh / 2
    }

    distance = {
        'x': pw / 2 + ew / 2,
        'y': ph / 2 + eh / 2
    }
    return center, distance


# 当たり判定
# IN:
#   -p: 自機データ
#   -e: ターゲット敵機データ
# RETURN:
#   -bool: 接触[True], 非接触[False]
# USE:
#   -calc_location()
def judge(p, e):
    c, d = calc_location(p, e)
    if abs(c['px'] - c['ex']) < d['x']:
        if abs(c['py'] - c['ey']) < d['y']:
            return True
    return False


def pro_judge(p, e, pimg, eimg):
    if judge(p, e):
        c, d = calc_location(p, e)

        # Collision Range
        cr_x = d['x'] - abs(c['px'] - c['ex'])
        cr_y = d['y'] - abs(c['py'] - c['ey'])

        p_cr = {'sx': 0, 'sy': 0, 'ex': 0, 'ey': 0}
        e_cr = {'sx': 0, 'sy': 0, 'ex': 0, 'ey': 0}

        # Locate Range
        if c['px'] - c['ex'] < 0:
            p_cr['sx'] = c['px'] - cr_x
            e_cr['sx'] = 0
        else:
            p_cr['sx'] = 0
            e_cr['sx'] = c['ex'] - cr_x

        if c['py'] - c['ey'] < 0:
            p_cr['sy'] = c['py'] - cr_y
            e_cr['sy'] = 0
        else:
            p_cr['sy'] = 0
            e_cr['sy'] = c['ey'] - cr_y

        # Is Not Transparent pixel in Collision Range?
        flags = [False, False]
        for x in range(p_cr['sx'], p_cr['ex']):
            for y in range(p_cr['sy'], p_cr['ey']):
                # Player
                if pick_colors(pimg, p_cr['sx'] + x, p_cr['sy'] + y)[3] > 0:
                    flags[0] = True

        for x in range(p_cr['sx'], p_cr['ex']):
            for y in range(p_cr['sy'], p_cr['ey']):
                # Enemy
                if pick_colors(eimg, e_cr['sx'] + x, e_cr['sy'] + y)[3] > 0:
                    flags[0] = True

        print(p, c, d, p_cr, e_cr)
        if flags[0] and flags[1]:
            return True
        else:
            return False


# 判定表示（警告）
# IN:
#   -player: 自機データ
#   -enemy_max: 敵機数
#   -enemies: 敵機データ
# OUT:
#   -None
# USE:
#   -judge()
def alert(player, enemy_max, enemies):
    for i in range(enemy_max):
        if judge(player, enemies[i]):
            print('敵機 {} が当たり'.format(i + 1))


def load_image(path):
    # 透過したい画像を読み込み
    org = Image.open(path)
    width = org.size[0]
    height = org.size[1]

    return org, width, height


def pick_colors(img, x, y):
    pixel = img.getpixel((x, y))
    return pixel