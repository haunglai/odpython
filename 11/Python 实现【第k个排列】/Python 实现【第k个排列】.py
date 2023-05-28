# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations

n, k = int(input()), int(input())
print("".join(map(str, list(permutations(range(1, n + 1), n))[k - 1])))