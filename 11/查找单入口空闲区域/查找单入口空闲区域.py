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

entrances = [-1, -1]
count = 0


def find_zone(m, n, x, y, coords, matrix):
    global entrances
    global count
    # 边界
    if (x == 0 or x == m - 1 or y == 0 or y == n - 1):
        count += 1  # 入口的数量计数
        entrances[0] = x
        entrances[1] = y

    # 往右或往下遍历
    if (x < m - 1):
        if (matrix[x + 1][y] == "O"):
            matrix[x + 1][y] = "X"
            coords.append([x + 1, y])
            find_zone(m, n, x + 1, y, coords, matrix)

    if (y < n - 1):
        if (matrix[x][y + 1] == "O"):
            matrix[x][y + 1] = "X"
            coords.append([x, y + 1])
            find_zone(m, n, x, y + 1, coords, matrix)


# 处理输入
m, n = map(int, input().split(" "))
matrix = []
for i in range(m):
    matrix.append(input().split(" "))

result = 0
empty_zones = []
for i in range(m):
    for j in range(n):
        if (matrix[i][j] == "O"):
            matrix[i][j] = "X"
            coords = []  # 空闲区域中的坐标集合
            coords.append([i, j])
            find_zone(m, n, i, j, coords, matrix)

            if (count == 1):
                if (result == len(coords)):  # 有大小相同的单入口空闲区域，只需要大小，无需坐标
                    empty_zones = []
                elif (result < len(coords)):
                    empty_zones = []
                    empty_zones.append([entrances[0], entrances[1], len(coords)])
                    result = len(coords)

            count = 0  # 重置入口数量
            entrances = [-1, -1]  # 重置入口坐标

# 输出
if (len(empty_zones) == 1):
    res = empty_zones[0]
    print(res[0] + " " + res[1] + " " + res[2])
elif (result != 0):
    print(result);
else:
    print("NULL")