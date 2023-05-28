# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

# 处理输入
params = [x for x in input().split(" ")]

scores = []

for i in range(len(params)):
    if (params[i] == "+"):
        scores.append(scores[len(scores) - 2] + scores[len(scores) - 1])
    elif (params[i] == "D"):
        scores.append(2 * scores[len(scores) - 1])
    elif (params[i] == "C"):
        scores.pop()
    else:
        scores.append(int(params[i]))

print(sum(scores))