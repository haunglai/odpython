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
input_str = "".join(input().split(" "))

# 无障碍物的区域
free_lines = input_str.split("2")

result = 0
for free_line in free_lines:
    # 左右连续1的个数
    counts = [len(x) for x in free_line.split("0")]

    temp = 0
    for i in range(len(counts)):
        temp = max(temp, counts[i - 1] + counts[i])
    result = max(result, temp)

print(result)


