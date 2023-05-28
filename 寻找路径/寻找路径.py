# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

# 处理输入
nodes = [int(x) for x in input().split(" ")]

ints = [-1 for x in range(len(nodes) + 1)]
minValue = max(nodes)
minPos = 0

for i in range(len(ints)):
    ints[i] = nodes[i - 1];
    # 找到最小叶子节点对应的索引
    if (i > 1 and ints[i] != -1 and ints[i] < minValue):
        minValue = ints[i]
        minPos = i

# 往上遍历
path = []
while (minPos >= 1):
    path.append(ints[minPos])
    minPos = int(minPos / 2)

print(" ".join([str(x) for x in path[::-1]]))