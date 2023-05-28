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

first_list = [int(x) for x in input().split()[1:]]
second_list = [int(x) for x in input().split()[1:]]
count = int(input())
pair_list = []
for i in first_list:
    for j in second_list:
        pair_list.append(i + j)
pair_list.sort()
print(sum(pair_list[:count]))