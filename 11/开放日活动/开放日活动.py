# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

# 处理输入
params = [int(x) for x in input().split(" ")]
sum_fixed = params[0]
count = params[1]
balls = [int(x) for x in input().split(" ")]

total = sum(balls)
if (total <= sum_fixed):
    print("[]")
else:
    tmp = [0 for x in range(count)]
    result = [0 for x in range(count)]
    # i 表示的就是最大容量
    i = sum_fixed
    while (True):
        for k in range(len(balls)):
            if (balls[k] > i):
                result[k] = balls[k] - i
                tmp[k] = i
            else:
                result[k] = 0
                tmp[k] = balls[k]

        if (sum(tmp) <= sum_fixed):
            print(result)
            break
        i -= 1