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

m = int(input())
while m > 0:
    m -= 1
    n = int(input())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append([y, x])
    a.sort(reverse=True)
    ans = 0
    now = 0
    for y, x in a:
        now += x
        ans = max(ans, now + y)
    print(ans)