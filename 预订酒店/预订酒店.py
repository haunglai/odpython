# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math


def comp(a, b):
    return a[1] - b[1]


params = [int(x) for x in input().split(" ")]
n = params[0]
k = params[1]
x = params[2]

# 先对价格排序
prices = [int(x) for x in input().split(" ")]
prices = sorted(prices)

price_rating = [];
for i in range(len(prices)):
    temp = []
    temp.append(prices[i])
    temp.append(abs(prices[i] - x))
    price_rating.append(temp)

# 自定义排序
sorted_prices = sorted(price_rating, key=functools.cmp_to_key(comp))

picked_price = []
for i in range(k):
    picked_price.append(sorted_prices[i][0])

picked_price = sorted(picked_price)

print(" ".join([str(x) for x in picked_price]))

