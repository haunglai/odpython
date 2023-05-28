# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re
import math

orders = input().split()
n, m = map(int, input().split())
if n == 0 or m == 0:
    print(0)
else:
    matrix = [input().split() for _ in range(n)]
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "H":
                x, y = i, j
                break
    res, command = 1, "L"
    for order in orders:
        ref = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
        if order == "G":
            if command in ref:
                dx, dy = ref[command]
                x, y = x + dx, y + dy
            if x < 0 or x >= n or y < 0 or y >= m or matrix[x][y] == "S":
                break
            if matrix[x][y] == "F":
                res += 1
                matrix[x][y] = "S"
        else:
            command = order
    print(res)