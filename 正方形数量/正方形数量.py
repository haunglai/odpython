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

point = []

for i in range(n):
    point.append(list(map(int, input().split(" "))))

point.sort(key=lambda x: (x[0], x[1]))

if n < 4:
    print(0)
else:
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            tmp_x = 0
            tmp_y = 0
            tmp_x = point[i][0] + point[i][1] - point[j][1]
            tmp_y = point[i][1] + point[j][0] - point[i][0]
            if ([tmp_x, tmp_y]) not in point:
                continue
            tmp_x = point[j][0] + point[i][1] - point[j][1]
            tmp_y = point[j][1] + point[j][0] - point[i][0]
            if ([tmp_x, tmp_y]) not in point:
                continue
            ans += 1
    print(int(ans / 2))