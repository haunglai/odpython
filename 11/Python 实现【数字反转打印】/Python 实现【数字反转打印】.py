# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re

n, res = int(input()), ""
for i in range(1, n + 1):
    big = (i + 1) * i // 2
    small = big + 1 - i
    if n == 1:
        res = "1" + "*" * 3
        continue
    cul_ls = list()
    for j in range(small, big + 1):
        length = 4 - len(str(j))
        cul_ls.append(f"{j}{'*' * length}")
    cul_ls = cul_ls if i % 2 != 0 else cul_ls[::-1]
    res += (n - i) * 4 * " " + (" " * 4).join(cul_ls) + "\n"

print(res)