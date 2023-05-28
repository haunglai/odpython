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


def set_false(start, end, data_a):
    for i in range(start, end + 1):
        data_a[i] = True


data_all = [False for i in range(4095)]
data_in = input().strip().split(',')
v_id = int(input().strip())
for i in data_in:
    if '-' in i:
        i_data = i.split('-')
        set_false(int(i_data[0]), int(i_data[1]), data_all)
    else:
        data_all[int(i)] = True
data_all[v_id] = False
res = ''
i = 1

while i < 4095:
    if data_all[i]:
        count = 1
        for j in range(i + 1, 4095):
            if data_all[j]:
                count += 1
            else:
                break
        if count > 1:
            res += str(i) + '-' + str(i + count - 1) + ','
            i += count - 1
        else:
            res += str(i) + ','
    i += 1
print(res[:-1])