# coding: utf-8
# Coding Skills: Kadai02
# 345(29) Daigo Miyajima

from FriAM_CodingSkills import Kadai02 as Poker

if __name__ == "__main__":
    data = [
        [0, 1], [3, 6], [3, 10], [3, 1], [1, 1]
    ]
    name = Poker.judge(data)
    Poker.result(data, name)
