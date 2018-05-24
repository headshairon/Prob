# Programmed by @headshairon_pad.
# You are not allowed to use it for commercial use.

import sub
# coding:utf-8
from decimal import *
from math import *
getcontext().prec = 100000

print(">>>>> *** ガチャ確率計算機 *** <<<<<")
print("魔法石 m 個を使用するガチャを n 回分回した時\n的中確率 p % のキャラクターが r 体以上出る確率を求めます")
print("計算の途中経過として回数をd分割して表示します")

m = sub.insertpositive("m")
n = sub.insertpositive("n")
p1 = sub.insertprob()
p2 = Decimal(100.0)
r = sub.insertpositive("r")
d = sub.insertpositive("d")

print( n ,"回 ( 約","{:.0f}".format(ceil(n*5000*m/85.0)),"円分 ) ガチャを回した時、\n的中確率", p1,"% のキャラクターが", r,"体以上出る確率")

listd = []
for i in range(1, d+1):
    listd.append(round(n*i/d))
sub.calc(n, r, p1, p2, m, listd)

print("*** 確率が低すぎる場合、括弧の中の数値は0％となります ***")
