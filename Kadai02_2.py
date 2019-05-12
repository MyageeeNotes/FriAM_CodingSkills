# coding: utf-8
# Coding Skills: Kadai02
# 345(29) Daigo Miyajima

from FriAM_CodingSkills import Kadai02 as Poker


if __name__ == "__main__":
    data = Poker.initialize(False)
    name = Poker.judge(data)
    Poker.result(data, name)
