# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re

n = int(input())
a = list(map(int, input().split()))
q = []
ans = [0] * n
for i in range(n - 1, -1, -1):
    while q and a[q[-1]] <= a[i]:
        q.pop()
    if q:
        ans[i] = q[-1]
    q.append(i)
print(*ans)