# coding: utf-8
# # Coding Skills: Kadai01-1
# # 課題１－１

import Kadai01 as ColDct

if __name__ == "__main__":

    # 課題用サンプルデータ
    kadai_data = "100 100 70 100\n3\n50 60 100 50\n10 120 100 50\n165 115 70 70"

    p, e_max, enms = ColDct.initialize(kadai_data)
    ColDct.alert(p, e_max, enms)