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

n, m = list(map(int, input().split()))
dishes = [list(map(int, input().split())) for i in range(n)]
times = sorted([sum(dish) for dish in dishes])
count = 1
for i in range(n):
    total, start, nxt = 1, i, i + 1
    while nxt < n:
        if times[nxt] - times[start] >= m:
            total += 1
            start = nxt
        nxt += 1
    if total > count:
        count = total
print(count)