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

n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split(" ")])

num_map = {}
for i in range(n):
    for j in range(m):
        # 将坐标转化为数组
        pos = [i, j]
        if (matrix[i][j] in num_map):
            num_map[matrix[i][j]].append(pos)
        else:
            num_map[matrix[i][j]] = []
            num_map[matrix[i][j]].append(pos)

resList = [];
for i in range(n):
    temp_list = []
    for j in range(m):
        pos_list = num_map[matrix[i][j]]
        # 无相等值
        if (len(pos_list) == 1):
            temp_list.append(-1);
            continue;

        min_distance = float("inf");
        for k in range(len(pos_list)):
            pos = pos_list[k]
            distance = abs(pos[0] - i) + abs(pos[1] - j);
            # 距离为0则跳过
            if (distance == 0):
                continue
            min_distance = min(min_distance, distance);

        temp_list.append(min_distance)

    resList.append(temp_list);

print(resList);
