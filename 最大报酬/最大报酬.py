# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

# 处理输入
params = [int(x) for x in input().split(" ")]
T = params[0]
n = params[1]
tasks = []
for i in range(n):
    tasks.append([int(x) for x in input().split(" ")])

# 从耗时最小的任务开始
min_time = T;
for task in tasks:
    min_time = min(min_time, task[0])

# dp
dp = [[0 for x in range(T + 1)] for y in range(n + 1)]

for i in range(n + 1):
    for j in range(min_time, T + 1):
        last = dp[i - 1][j]
        if tasks[i - 1][0] > j:
            current = 0
        else:
            current = tasks[i - 1][1] + dp[i - 1][j - tasks[i - 1][0]]
        dp[i][j] = max(last, current)

print(dp[n][T])