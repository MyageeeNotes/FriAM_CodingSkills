# coding: utf-8
# Coding Skills: Kadai02
# 345(29) Daigo Miyajima

import random


def initialize(jf):
    dt = []
    for i in range(5):
        if jf:
            dt.append([0, random.randint(1, 14)])
            if [0, 14] in dt:
                jf = False
        else:
            dt.append([0, random.randint(1, 13)])

    for i in range(5):
        if dt[i][1] == 14:
            dt[i][0] = 4
        else:
            suit = random.randint(0, 3)
            dt[i][0] = suit
            for j in range(i):
                if dt[i] == dt[j]:
                    var = dt[i][0]
                    dt[i][0] = (var + 1) % 4

    return dt


def convert(card):
    suit, number = card
    suit_char = ['S', 'C', 'D', 'H', 'J']
    num_char = ['A', 'J', 'Q', 'K', 'R']

    if number == 1:
        number = num_char[0]
    elif number >= 11:
        number = num_char[number - 10]

    return [suit_char[suit], number]


def count_pairs(nd, ps, mx):
    pair = 0
    for i in range(4):
        pair = 0
        parent = nd[i]
        # Find Same number
        for j in range(i + 1, 5):
            child = nd[j]
            if parent == child:
                pair += 1
        # count pair
        if pair != 1:
            ps += 1
        # same numbers count
        if ps > mx:
            mx = ps
    return mx, pair


def has_same_name(num_data):
    max_pair = 0
    pair = 0
    pairs = 0

    for cnt in range(1, 13):
        for i in range(4):
            max_pair, pair = count_pairs(num_data, pairs, max_pair)

    return max_pair, pair


def is_stairs(num_data):
    # has JOKER?
    joker = False
    if 14 in num_data:
        joker = True
        num_data.remove(14)

    sorted_list = sorted(num_data)
    parent = sorted_list[0]
    if parent == 1:
        for i in range(sorted_list[-1] - 9):
            sorted_list[i] += 13
        sorted_list = sorted(sorted_list)
        parent = sorted_list[0]
    distance = [s - parent for s in sorted_list]

    if distance == [0, 1, 2, 3, 4]:
        if parent == 10:
            # Royal flag
            return True, 1
        else:
            return True, 0
    elif joker:
        dist_cnt = 0
        for i in range(5):
            if i in distance:
                dist_cnt += 1
        if dist_cnt == 4:
            if parent == 10 or parent == 11:
                return True, 1
            else:
                return True, 0
        else:
            return False, 0
    else:
        return False, 0


def judge(dt):
    nm = [
        'ハイカード',  # 0-: default
        'ワンペア',  # 1: 2 same-NUM
        'ツーペア',  # 2: 2 same-NUM pair
        'スリーカード',  # 3: 3 same-NUM
        'フルハウス',  # 4-: 3 and 2 same-NUM
        'フォーカード',  # 5-: 4 same-NUM
        'ストレート',  # 6: stairs
        'フラッシュ',  # 7: all same-SUIT
        'ストレートフラッシュ',  # 8: same-SUIT stairs
        'ロイヤルフラッシュ'  # 9: same-SUIT 10 - A
    ]

    # has JOKER?
    joker = False
    if [4, 14] in dt:
        joker = True
    # has number's PAIR ?
    num_dt = [s[1] for s in dt]
    pair_list = list(dict.fromkeys(num_dt))
    pair_list_num = len(pair_list)

    suit_dt = [s[0] for s in dt]
    suit_list = list(dict.fromkeys(suit_dt))
    suit_list_num = len(suit_list)
    same_suit = False
    if suit_list_num == 1:
        same_suit = True
    elif suit_list_num == 2 & joker:
        sl_cnt = suit_list.count(suit_list[0])
        if sl_cnt == 1 or sl_cnt == 4:
            same_suit = True

    # Four cards
    if pair_list_num == 1:
        return nm[5]
    # Full House
    elif pair_list_num == 2:
        return nm[4]
    # Two pairs or Three card
    elif pair_list_num == 3:
        max_pair, num = has_same_name(num_dt)
        if max_pair == 3:
            if joker:
                return nm[5]
            return nm[3]
        else:
            if joker:
                return nm[3]
            return nm[2]
    # One pair
    elif pair_list_num == 4:
        if joker:
            return nm[3]
        return nm[1]
    # else
    elif pair_list_num == 5:
        stairs_judge = is_stairs(num_dt)
        if stairs_judge[0]:
            # Royal Straight Flash
            if stairs_judge[1] == 1:
                if same_suit:
                    return nm[9]
                return nm[6]
            else:
                if same_suit:
                    return nm[8]
                else:
                    return nm[6]
        else:
            if same_suit:
                return nm[7]
            else:
                if joker:
                    return nm[1]
                return nm[0]


def result(dt, nm):
    display = ''
    for i in range(5):
        var = convert(dt[i])
        display += (var[0] + str(var[1]) + ' ')
    display = display[:-1]
    print(display)
    print(nm)


def battle(dt):
    pt = [
        'ハイカード',  # 0
        'ワンペア',  # 1
        'ツーペア',  # 2
        'スリーカード',  # 3
        'ストレート',  # 4
        'フラッシュ',  # 5
        'フルハウス',  # 6
        'フォーカード',  # 7
        'ストレートフラッシュ',  # 8
        'ロイヤルフラッシュ'  # 9
    ]
    return pt.index(dt)