# coding: utf-8
# Coding Skills: Kadai02
# 345(30)

from FriAM_CodingSkills.Kadai02_Poker import Kadai02 as Poker

if __name__ == "__main__":
    data = [
        [0, 1], [3, 6], [3, 10], [3, 1], [1, 1]
    ]
    name = Poker.judge(data)
    Poker.result(data, name)
