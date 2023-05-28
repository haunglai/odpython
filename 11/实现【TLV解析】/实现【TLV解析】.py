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

n, tvls = input(), input().split()
i = 0
flag = True
while i < len(tvls):
    pos = tvls[i]
    j = i + 3
    temp = tvls[i + 1:j]
    mid = int("".join(temp[:: -1]), base=16)
    res = tvls[j:mid + j]
    if pos == n:
        print(" ".join(res))
        flag = False
        break
    else:
        i += mid + 3
if flag:
    print("")