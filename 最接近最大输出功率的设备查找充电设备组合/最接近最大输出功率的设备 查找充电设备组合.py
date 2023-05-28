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

# 处理输入
n = int(input())
p = [int(x) for x in input().split(" ")]
p_max = int(input())

# dp[i][j] 表示从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少。
dp = [[0 for x in range(p_max + 1)] for y in range(n + 1)]

# 初始化, i为0，存放编号0的物品的时候，各个容量的背包所能存放的最大价值。
j = p_max
while (j >= p[0]):
    dp[0][j] = dp[0][j - p[0]] + p[0]
    j -= 1

for i in range(1, n):  # 遍历物品
    for j in range(0, p_max + 1):  # 遍历背包容量
        # 背包容量为j，如果物品i的体积，此时dp[i][j]就是dp[i - 1][j]
        if (j < p[i]):
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - p[i]] + p[i])

print(dp[n - 1][p_max])




