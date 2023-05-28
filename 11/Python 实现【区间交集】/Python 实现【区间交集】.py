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

# input
ranges = []
for line in sys.stdin:
    a = line.split()
    left = int(a[0])
    right = int(a[1])
    ranges.append((left, right))

ORI_LEN = len(ranges)
LEN = len(ranges)
pre_LEN = LEN + 1

# find out intersection
new_ranges = set()
for i in range(LEN):
    for j in range(i + 1, LEN):
        if ranges[i][1] >= ranges[j][0]:
            left = max(ranges[i][0], ranges[j][0])
            right = min(ranges[i][1], ranges[j][1])
            if left <= right:
                new_ranges.add((left, right))

ranges = list(new_ranges)
ranges.sort()

# find out union
new_ranges = set()
LEN = len(ranges)
for i in range(LEN):
    if ranges[i] == None:
        continue
    left = ranges[i][0]
    right = ranges[i][1]
    for j in range(i + 1, LEN):
        if ranges[j] == None:
            continue

        if ranges[j][0] <= right:
            right = max(right, ranges[j][1])
            ranges[j] = None
        else:
            break
    new_ranges.add((left, right))

ranges = list(new_ranges)
ranges.sort()

if len(ranges) == 0:
    print("None")
else:
    for l, r in ranges:
        print(f"{l} {r}")

