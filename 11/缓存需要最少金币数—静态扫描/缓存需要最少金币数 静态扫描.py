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


def comp(a, b):
    return b[1] - a[1]


# 处理输入
m = int(input())

file_ids = [int(x) for x in input().split(" ")]
sizes = [int(x) for x in input().split(" ")]

# key为文件标识 value为文件出现的次数
file_map = {}
# key为文件标识 value为扫描成本
file_cost = {}

for i in range(len(file_ids)):
    if (file_ids[i] in file_map):
        file_map[file_ids[i]] += 1
    else:
        file_map[file_ids[i]] = 1
    file_cost[file_ids[i]] = sizes[i]

result = 0
for key in file_map:
    result += min(file_map[key] * file_cost[key], file_cost[key] + m)

print(result)