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

ans = []


def check(s):
    a = ['late', 'leaveearly']
    for i in a:
        for j in a:
            if s.find(i + ' ' + j) != -1:
                return False
            elif s.find(j + ' ' + i) != -1:
                return False
    logs = s.split()
    m = len(logs)
    cnt = 0
    for i in logs:
        if i == 'absent':
            cnt += 1
    if cnt > 1:
        return False
    for i in range(m):
        cnt = 0
        for j in range(i, min(i + 7, m)):
            if logs[j] in ['absent', 'leaveearly', 'late']:
                cnt += 1
        if cnt > 3:
            return False
    return True


for i in range(n):
    if check(input()):
        ans.append('true')
    else:
        ans.append('false')
print(' '.join(ans))