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

n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

dps = 0
last = -1

for i in range(n):
    if last != -1:
        cost[i][last] = float('inf')
    cur = min(cost[i])
    dps += cur
    for j in range(3):
        if cost[i][j] == cur:
            last = j

print(dps)