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

s = input()

i = 0
LEN = len(s)
ans = []
s = s.lower()

while i < LEN:
    c = s[i]
    t = i
    if i < LEN - 1 and s[i] == s[i + 1]:
        while i < LEN - 1 and s[i] == s[i + 1]:
            i += 1
        i += 1
        ans.append(c)
        ans.append(str(i - t))
    else:
        ans.append(c)
        ans.append("1")
        i += 1

print(''.join(ans))
