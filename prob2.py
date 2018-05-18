import sub
# coding:utf-8
from decimal import *
from math import *
getcontext().prec = 100000

print(">>>>> *** ガチャ確率計算機 *** <<<<<")
print("5000円 n セット分ガチャを回した時、\n的中確率 p % のキャラクターが r 体以上出る確率を求めます")
print("計算の途中経過として回数を1セットごとに表示します")

n = sub.insertpositive("n")
n = (n + 1) * 17
r = sub.insertpositive("r")
p1 = sub.insertprob()
p2 = Decimal(100.0)

print("5000円", n,"セット分 (", n - 17 ,"回) ガチャを回した時、\n的中確率", p1,"% のキャラクターが", r,"体以上出る確率")
listd = range(17, n, 17)
sub.calc(n, r, p1, p2, listd)

print("*** 確率が低すぎる場合、括弧の中の数値は0％となります ***")
