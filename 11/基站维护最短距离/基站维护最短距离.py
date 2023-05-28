# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math


def solve(n, matrix):
    dp = [[float('inf') for x in range(1 << n)] for y in range(n)]
    for i in range(n):
        dp[i][1 << i] = matrix[0][i]

    # j为当前状态
    for j in range(1 << n):
        # i为当前基站
        for i in range(n):
            if ((j & (1 << i)) == 0):
                continue  # 注意运算符优先级
            # k为下一个基站
            for k in range(n):
                dp[i][j] = min(dp[i][j], dp[k][j & (~(1 << i))] + matrix[k][i])

    return dp[0][(1 << n) - 1];


n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split(" ")])
# print(matrix)
print(solve(n, matrix))
