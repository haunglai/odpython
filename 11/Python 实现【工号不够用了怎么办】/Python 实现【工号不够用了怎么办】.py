# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy


def solve(x, y):
    z = 1
    base = pow(26, y)
    factor = 10
    while (True):
        if base * factor >= x:
            return z
        z += 1
        factor *= 10


# 处理输入
x, y = map(int, input().split())
print(solve(x, y))
