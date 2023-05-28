# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re
import math

cards = list(map(int, input().strip().split(',')))
count = 0
tmplist = []
for i in range(len(cards)):
    if i < 3:
        count += cards[i]
        if count <= 0:
            count = 0
        tmplist.append(count)
    else:
        count += cards[i]
        if count >= tmplist[i - 3]:
            tmplist.append(count)
        else:
            count = tmplist[i - 3]
            tmplist.append(tmplist[i - 3])
print(tmplist[-1])