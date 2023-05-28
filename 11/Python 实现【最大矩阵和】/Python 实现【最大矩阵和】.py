# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

n, m = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append([int(x) for x in input().split(" ")])

ans = -1000

for i in range(n):
    b = [0] * m
    for j in range(i, n):
        sum = 0
        for k in range(m):
            b[k] += matrix[j][k]
            if sum > 0:
                sum += b[k]
            else:
                sum = b[k]
            if sum > ans:
                ans = sum
print(ans)