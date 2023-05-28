# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math

list1 = input().split()
rule = input()
res = list()
for p in rule:
    if p == "*":
        res.extend(["(", ".", "*", ")"])
        continue
    res.append(p)
rule = "".join(res)
ans = [str(i) for i in range(len(list1)) if re.match(rule, list1[i])]

print(",".join(ans) if ans else 0)