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

str_input = input()
res = list(str_input)
if str_input.isalpha():
    i = 1
    while True:
        if i >= len(res):
            break
        elif i > 0 and res[i] == res[i - 1]:
            res.pop(i)
            res.pop(i - 1)
            i -= 2
        i += 1
    print(len(res))
else:
    print(0)