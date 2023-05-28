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
link = []
for i in range(n):
    input_temp = tuple(map(int, input().split()))
    link.append(input_temp)

# 去重
link = list(set(link))

node_to = []
node_from = []

for node in link:
    node_to.append(node[0])
    node_from.append(node[1])

node_to.sort()
node_from.sort()

print(node_to == node_from)