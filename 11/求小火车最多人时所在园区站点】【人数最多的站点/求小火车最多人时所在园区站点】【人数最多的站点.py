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


# 人数
n = int(input())

# key为站点，value为站点的人数
site_map = {}
for i in range(n):
    params = [int(x) for x in input().split(" ")]
    start = min(params[0], params[1])
    end = max(params[0], params[1])
    for j in range(start, end + 1):
        if (j in site_map):
            site_map[j] += 1
        else:
            site_map[j] = 1

# 将map信息转到list中，以便后续排序
sites = []
for key in site_map:
    sites.append([key, site_map[key]]);

sites = sorted(sites, key=functools.cmp_to_key(comp));

# 输出
print(sites[0][0])
