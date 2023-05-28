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

m, n = list(map(int, input().split()))
tasks = sorted(list(map(int, input().split())))
pos, total = 0, 0
task = tasks[0:m]
for i in tasks[m:]:
    pos = task[0]
    total += pos
    task = [i - pos for i in task]
    task[0] = i
    task.sort()
total = total + task[-1]
print(total)