import sub
# coding:utf-8
from decimal import *
from math import *
getcontext().prec = 100000

print(">>>>> *** ガチャ確率計算機 *** <<<<<")
print(" n 回ガチャを回した時\n的中確率 p % のキャラクターが r 体以上出る確率を求めます")
print("計算の途中経過として回数をd分割して表示します")

n = sub.insertpositive("n")
r = sub.insertpositive("r")
p1 = sub.insertprob()
p2 = Decimal(100.0)
d = sub.insertpositive("d")

print( n ,"回 (","{:.0f}".format(Decimal(n*5000/17)),"円分 ) ガチャを回した時、\n的中確率", p1,"% のキャラクターが", r,"体以上出る確率")

listd = []
for i in range(1, d+1):
    listd.append(round(n*i/d))
sub.calc(n, r, p1, p2, listd)

print("*** 確率が低すぎる場合、括弧の中の数値は0％となります ***")
