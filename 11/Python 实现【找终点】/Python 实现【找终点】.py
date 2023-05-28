# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re
import math

str = input()
strs = str.split(" ")
arr = [int(item) for item in strs]

num = len(arr)
max_int = 1 << 31
dp = [max_int for i in range(num)]
dp[0] = 0
for i in range(1, int(num / 2)):
    dp[i] = 1

    if (i + arr[i] < num):
        dp[i + arr[i]] = min(2, dp[i + arr[i]])
for i in range(int(num / 2), num):
    if (i + arr[i] < num):
        dp[i + arr[i]] = min(dp[i + arr[i]], dp[i] + 1)

if dp[num - 1] == max_int:
    print(-1)
else:
    print(dp[num - 1])