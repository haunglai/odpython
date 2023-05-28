# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

# 处理输入
count = int(input())
nodes = [int(x) for x in input().split(" ")]
nodes = sorted(nodes)
print(nodes[int(count / 2)])