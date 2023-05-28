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

a = input().strip()
last = ' '
res = 0
cnt = 0
for letter in a:
    if letter != last:
        if res < cnt:
            res = cnt
        last = letter
        cnt = 1
    else:
        cnt += 1

if res < cnt:
    res = cnt

print(res)
