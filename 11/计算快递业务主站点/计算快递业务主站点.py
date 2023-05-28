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


def check(site_set, n, matrix):
    for i in range(len(matrix)):
        if (i in site_set):
            continue
        if (n != i and matrix[n][i] == 1):
            site_set.add(i)
            check(site_set, i, matrix)


# 处理输入
N = int(input())
matrix = []
for i in range(N):
    matrix.append([int(x) for x in input().split(" ")])

# 已经有连通的站点
site_set = set()
# 需要遍历的次数
res = 0
for i in range(N):
    # 当前站点已经可以达到
    if (i in site_set):
        continue
    temp = set()
    temp.add(i)
    check(temp, i, matrix)
    site_set = set.union(site_set, temp)
    res += 1

print(res)