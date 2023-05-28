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

n, m = map(int, input().split())
ref = {i + 1: {} for i in range(n)}
for i in range(m):
    u, v = map(int, input().split())
    ref[u][v] = 1
    ref[v][u] = 1
begin = int(input())
seen = [0] * (n + 1)
seen[begin] = 1
count, q = 0, [begin]
while True:
    temp = list()
    for item in q:
        for key in ref[item]:
            if seen[key] == 0:
                seen[key] = 2
                temp.append(key)
    if not temp:
        break
    q, count = temp, count + 1
print(count * 2)