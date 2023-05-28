# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math


def is_normal(matrix, errors):
    temp = errors
    for error in errors:
        if error not in matrix.keys():
            continue
        else:
            for value in matrix[error]:
                if value not in temp:
                    temp.append(value)
    if errors != temp:
        is_normal(matrix, temp)
    else:
        return errors


relation, errors = input().split(","), input().split(",")
matrix, items = defaultdict(list), list()
for r in relation:
    a, b = r.split("-")
    for x in [a, b]:
        if x not in items:
            items.append(x)
    matrix[b].append(a)
ret = is_normal(matrix, errors)
normal = [item for item in items if item not in ret]
print(",".join(normal) if normal else ",")