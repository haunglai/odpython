# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math
import sys


def cmp(x, y):
    if x[1] == y[1]:
        return y[0] - x[0]
    else:
        return y[1] - x[1]


# 处理输入
nums = [int(x) for x in input().split(" ")]

# key为牌面点数，value为该点数的张数
card_info = {}
for num in nums:
    if num in card_info:
        card_info[num] += 1
    else:
        card_info[num] = 1

# 排序，先按张数排序，再按点数排序
card_info_list = sorted(card_info.items(), key=functools.cmp_to_key(cmp))

# 特殊情况处理
result = ""
split_cards = []
for i in range(len(card_info_list)):
    temp = card_info_list[i]
    carNum = temp[0]
    carCount = temp[1]
    # 3+3的情况，要拆分成葫芦
    if (i > 0 and card_info_list[i - 1][1] == 3 and carCount == 3):
        split_cards.append(carNum)
        carCount = 2
        temp = (temp[0], 2)
    # 给拆分的牌也组合一下
    elif (carCount == 1 and split_cards.size() != 0):
        for k in range(len(split_cards)):
            # 当拆分中的牌大于此牌时，先安排拆分的牌
            if (split_cards[k] > carNum):
                result += str(split_cards[k]) + " "
                split_cards.pop(k)
                k -= 1

    for j in range(carCount):
        result += str(carNum) + " "

if (len(split_cards) != 0):
    for card in split_cards:
        result += str(i) + " "

print(result)