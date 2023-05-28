# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

m, n, dis = map(int, input().split())
set_a = [int(x) for x in input().split()]
set_b = [int(x) for x in input().split()]

i, j = 0, 0
temp = list()
while True:
    if i >= m or j >= n:
        break
    if set_b[j] - set_a[i] < 0:
        j += 1
    else:
        if set_b[j] - set_a[i] <= dis:
            temp.append((set_a[i], set_b[j]))
        i += 1

for i, j in temp:
    print(i, j)