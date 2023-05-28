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


def cmx(x, y):
    a = abs(H - x)
    b = abs(H - y)
    if a < b:
        return -1
    if a == b:
        if x < y:
            return -1
        if x > y:
            return 1
        return 0
    return 1


H, n = map(int, input().split())

arr = [int(i) for i in input().split()]
newList = sorted(arr, key=functools.cmp_to_key(cmx))
for i in newList:
    print(i, end=" ")