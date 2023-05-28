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


def recur(n):
    if n in [0, 1]:
        return 0
    return recur(n // 2) + 1 if n % 2 == 0 else min(recur(n + 1), recur(n - 1)) + 1


print(recur(int(input())))