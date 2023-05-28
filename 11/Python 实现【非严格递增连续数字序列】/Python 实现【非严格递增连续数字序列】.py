# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations

strs = input().strip()
i = 0
pos = 0
res_list = [0]
while i < len(strs):
    if strs[i] >= '0' and strs[i] <= '9':
        if i >= 0 and strs[i - 1] > strs[i]:
            pos = i
        res_list.append(i - pos + 1)
    i += 1
print(max(res_list))