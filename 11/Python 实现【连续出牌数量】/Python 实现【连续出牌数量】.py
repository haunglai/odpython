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


def dfs(numbers, colors, last_num, last_color, card):
    maxdepth = 0
    for i in range(len(card)):
        if card[i] != 0:
            if numbers[i] == last_num or colors[i] == last_color:
                card[i] = 0
                maxdepth = max(dfs(numbers, colors, numbers[i], colors[i], card), maxdepth)
                card[i] = 1
    return maxdepth + 1


number_str = input().split(' ')
color_str = input().split(' ')
cards = [1 for i in range(len(number_str))]
maxiter = 0
for i in range(len(number_str)):
    cards[i] = 0
    maxiter = max(dfs(number_str, color_str, number_str[i], color_str[i], cards), maxiter)
    cards[i] = 1
print(maxiter) 