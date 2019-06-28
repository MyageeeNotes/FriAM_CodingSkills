# coding: utf-8
# Coding Skills: Kadai02
# 345(30)

from FriAM_CodingSkills.Kadai02_Poker import Kadai02 as Poker

if __name__ == "__main__":

    point = [0, 0]
    joker_flag = False

    print("TURN: Opponent")
    data, joker_flag = Poker.initialize(joker_flag)
    name = Poker.judge(data)
    Poker.result(data, name)
    point[0] = Poker.battle(name)

    print("\nTURN: YOU")
    data, joker_flag = Poker.initialize(joker_flag)
    name = Poker.judge(data)
    Poker.result(data, name)
    point[1] = Poker.battle(name)

    print()
    if point[0] < point[1]:
        print("You WIN!!")

    elif point[0] > point[1]:
        print("You LOSE...")

    else:
        print("-- DRAW --")
