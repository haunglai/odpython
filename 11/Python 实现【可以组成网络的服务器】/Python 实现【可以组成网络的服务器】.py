# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re
import math


def cal(node, network):
    x, y = node
    if node in network:
        network.remove(node)
        group[-1].append(node)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in network:
                cal((new_x, new_y), network)


n, m = list(map(int, input().split()))
server = [list(map(int, input().split())) for _ in range(n)]
network = list()
for i, x in enumerate(server):
    network.extend([(i, j) for j, y in enumerate(x) if y == 1])
group = []
for node in network:
    group.append([])
    cal(node, network)
print(max([len(i) for i in group]))