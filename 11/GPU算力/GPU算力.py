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

task_num, n = int(input()), int(input())
tasks = list(map(int, input().split()))
num = total = 0
for task in tasks:
    total += task - task_num
    num += 1
    if task < task_num:
        total = 0 if total < 0 else total
        continue
pos = math.ceil(total / task_num)
print(pos + num)