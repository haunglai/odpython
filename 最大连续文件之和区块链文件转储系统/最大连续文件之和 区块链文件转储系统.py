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

# 处理输入
M = int(input())

F = [int(x) for x in input().split(" ")]

# 窗口左右边界
left = 0
right = 0
# 窗口和
window_sum = 0
# 最大窗口和
window_max = 0

find_M_flag = False
while (right < len(F)):
    temp = window_sum + F[right]

    # 窗口内总和大了，sum减去左边界，左端边界+1
    if (temp > M):
        window_sum -= F[left]
        left += 1

    # 窗口内总和小了，右边界+1，sum加上右边界
    elif (temp < M):
        window_sum += F[right]
        window_max = max(window_sum, window_max)
        right += 1

    # 窗口内总和==M，直接return
    else:
        print(M)
        find_M_flag = True
        break

if not find_M_flag:
    print(window_max)




