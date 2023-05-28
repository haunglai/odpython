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

nums = [int(x) for x in input().split(',')]
k = int(input())
nums = sorted(list(set(nums)))

visited = {}
res = []


def dfs(pos, cur):
    global nums
    global k
    if len(cur) >= k:
        ans = ','.join(cur)
        if visited.get(ans) is None:
            res.append(ans)
            visited[ans] = True
    if pos >= len(nums):
        return
    cur.append(str(nums[pos]))
    dfs(pos + 1, cur)
    cur.pop()
    dfs(pos + 1, cur)


dfs(0, [])

if len(res) == 0:
    print('None')
else:
    res = sorted(res)
    print('\n'.join(res))

