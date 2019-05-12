# coding: utf-8
# Coding Skills: Kadai02
# 345(29) Daigo Miyajima

from FriAM_CodingSkills import Kadai02 as Poker


if __name__ == "__main__":
    joker_flag = False
    data, joker_flag = Poker.initialize(joker_flag)
    name = Poker.judge(data)
    Poker.result(data, name)
