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

m, n = map(int, input().split(','))
M = []
for i in range(m):
    M.append([1 if i == 'M' else 0 for i in input().split(',')])

dp = [[[0] * 4 for _ in range(n + 2)] for _ in range(m + 2)]
ans = 0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if M[i - 1][j - 1] == 1:
            dp[i][j][0] = dp[i - 1][j][0] + 1
            dp[i][j][1] = dp[i][j - 1][1] + 1
            dp[i][j][2] = dp[i - 1][j - 1][2] + 1
            dp[i][j][3] = dp[i - 1][j + 1][3] + 1
            ans = max(ans, max(dp[i][j]))
print(ans)