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

s, t = input().split()
now = [0] * 26
for c in s:
    now[ord(c) - 97] += 1

cnt = [[0] * 26 for _ in range(len(t) + 1)]
for i in range(1, len(t) + 1):
    for j in range(26):
        cnt[i][j] = cnt[i - 1][j]
    cnt[i][ord(t[i - 1]) - 97] += 1

ans = -1
for i in range(len(t) - len(s) + 1):
    flag = True
    for j in range(26):
        if cnt[i + len(s)][j] - cnt[i][j] != now[j]:
            flag = False
    if flag:
        ans = i
        break
print(ans)