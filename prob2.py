# Programmed by @headshairon_pad.
# You are not allowed to use it for commercial use.

import sub
# coding:utf-8
from decimal import *
from math import *
getcontext().prec = 100000

print(">>>>> *** ガチャ確率計算機 *** <<<<<")
print("魔法石 m 個を使用するガチャを 5000円 n セット分ガチャを回した時、\n的中確率 p % のキャラクターが r 体以上出る確率を求めます")
print("計算の途中経過として回数を1セットごとに表示します")

Flag = True
while Flag:
    m = sub.insertpositive("m")
    t = sub.insertpositive("n")
    n = floor(t * 85 / m)
    print(n)
    p1 = sub.insertprob()
    p2 = Decimal(100.0)
    r = sub.insertpositive("r")


    print("5000円", t,"セット分 (", n ,"回) ガチャを回した時、\n的中確率", p1,"% のキャラクターが", r,"体以上出る確率")
    listd = []
    for i in range(1, t):
        listd.append(round(i*85/m))
    listd.append(n)
    sub.calc(n, r, p1, p2, m, listd)

    print("*** 確率が低すぎる場合、括弧の中の数値は0％となります ***")
    Flag = sub.iscontinue()
