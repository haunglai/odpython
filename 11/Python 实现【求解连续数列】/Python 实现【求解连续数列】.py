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

s, n = map(int, input().split())

total = (1 + n) * n // 2
if s >= total and (s - total) % n == 0:
    k = (s - total) // n
    ans = []
    for i in range(n):
        ans.append(str(i + k + 1))
    print(' '.join(ans))
else:
    print(-1)

