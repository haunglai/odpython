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

N = int(input().strip())
ids = list(map(int, input().strip().split(",")))
sums = list(map(int, input().strip().split(",")))
table, total, res = defaultdict(list), defaultdict(list), list()
for i in range(N):
    table[ids[i]].append(sums[i])
for idd in table:
    temp = table[idd]
    if len(temp) >= 3:
        temp.sort(reverse=True)
        total[sum(temp[:3])].append(idd)
sums = sorted(total.items(), key=lambda x: x[0], reverse=True)
for _, score in sums:
    res += sorted(score, reverse=True)
print(",".join(map(str, res)))