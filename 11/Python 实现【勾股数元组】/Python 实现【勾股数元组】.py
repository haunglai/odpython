# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re
import math

start = int(input())
end = int(input())
LEN = math.ceil(math.sqrt(end))

ans = []

for i in range(1, LEN):
    for j in range(i + 1, LEN):
        if math.gcd(i, j) != 1:
            continue

        a = j ** 2 - i ** 2
        b = 2 * i * j
        if a < start or b < start:
            continue
        c = i ** 2 + j ** 2
        if c <= end:
            if math.gcd(a, b) == 1 and math.gcd(a, c) == 1 and \
                    math.gcd(b, c) == 1:
                t = [a, b, c]
                t.sort()
                ans.append(t)

if len(ans) > 0:
    ans.sort()
    for t in ans:
        print(f"{t[0]} {t[1]} {t[2]}")
else:
    print("NA")