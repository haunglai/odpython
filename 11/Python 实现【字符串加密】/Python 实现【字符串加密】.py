# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re
import math

n = int(input().strip())
code = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
list = []
offset = [1, 2, 4] + [0] * 48
for i in range(3, 50):
    offset[i] = offset[i - 1] + offset[i - 2] + offset[i - 3]
for _ in range(n):
    data = input().strip()
    list.append(data)
for i in range(n):
    res = ''
    for j in range(len(list[i])):
        f = offset[j] % 26
        res += code[code.index(list[i][j]) + f]
    print(res)