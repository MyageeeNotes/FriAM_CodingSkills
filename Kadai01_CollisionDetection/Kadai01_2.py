# coding: utf-8
# Coding Skills: Kadai01-2
# 課題１－２

import Kadai01 as ColDct


data = "1000 1000 400 600\n3\n200 1300 830 390\n370 1300 830 390\n500 900 830 390"
p, e_max, enms = ColDct.initialize(data)

pimg, pw, ph = ColDct.load_image('images/rocket.png')
eimg, ew, eh = ColDct.load_image('images/enemy.png')

for i in range(e_max):
    if ColDct.pro_judge(p, enms[i], pimg, eimg):
        print('敵機 {} が当たり'.format(i + 1))