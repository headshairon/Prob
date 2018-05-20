# coding:utf-8
from decimal import *
from math import *
getcontext().prec = 100000

def is_float(s):
  try:
    float(s)
  except:
    return -1
  return float(s)

def is_prob(s):
    if is_float(s) != -1 :
        s = Decimal(s)
        if 0.0 <= s and s <= 100.0 :
            return s
    return -1

def bin(n, r):
    m = Decimal(1)
    if n < 2 * r:
        r = n - r
    for i in range(1, r + 1):
        m = Decimal(m) * Decimal(n - i + 1) / Decimal(i)
    return Decimal(m)

def binthm(n, r, p1, p2):
    tmp = Decimal(((p2-p1)/p2)**Decimal(r))*Decimal((p1/p2)**(Decimal(n)-Decimal(r)))*bin(n,r)
    return tmp

def insertpositive(c):
    print(c, "= ", end = "")
    n = is_float(input())
    k = floor(n)
    while k <= 0:
        print("1以上の正の整数値を入力してください")
        n = is_float(input("n = "))
        k = floor(n)
    else :
        if n - k != 0 :
            print("小数部は切り捨てます")
            return k
        else :
            return int(n)

def insertprob():
    p1 = is_prob(input("確率をパーセンテージで入力 :"))
    while p1 == -1:
        print("0以上100以下の正の整数値を入力してください")
        p1 = sub.is_prob(input("確率をパーセンテージで入力 :"))
    else:
        return Decimal(p1)

def calc(n, r, p1, p2, listd):
    for i in listd:
        if i < r:
            print("{0:7d}".format(int(i*5000/17)),"円分:","impossible.")
            continue

        num = Decimal(0.0)
        for number in range(0, r) :
            num = num + binthm(i, i - r + 1 + number, p1, p2);
        num = (Decimal(1.0) - num) * 100

        print("{:8.0f}".format(Decimal(i*5000/17)),"円分: ガチャ","{0:4d}".format(i),"回分: ",'{:.8e}'.format(num),"(",'{:.8f}'.format(num),") %")
