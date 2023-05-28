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

rm_list_all = []


def find_rm(rm_pv, tree_):
    rm_list_all.append(rm_pv)
    if tree_.get(rm_pv):
        for i in tree_.get(rm_pv):
            find_rm(i, tree_)


lines = int(input().strip())
tree = {}
for i in range(lines):
    s, p = [int(i) for i in input().strip().split()]
    if tree.get(p) is None:
        tree[p] = [s]
    else:
        tree[p].append(s)
rm_p = int(input().strip())
find_rm(rm_p, tree)
res = []

for k, v in tree.items():
    if k not in rm_list_all and k != 0:
        res.append(k)
    for i in v:
        if i not in rm_list_all and i != 0:
            res.append(i)
res = list(set(res))
res.sort()
print(' '.join([str(i) for i in res]))