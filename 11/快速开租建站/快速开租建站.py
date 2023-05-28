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
taskNum = int(input())
relationsNum = int(input())
relation_ids = []
for i in range(relationsNum):
    relation_ids.append([int(x) for x in input().split(" ")])

# 每个任务的前置依赖任务个数，也就是拓扑排序中的入度
upstream = [0 for x in range(relationsNum)]
# 每个任务的下游任务， 也就是拓扑排序中的出度
downstream = [[] for x in range(relationsNum)]

# 初始化入度、出度
for relation_id in relation_ids:
    downstream[relation_id[0]].append(relation_id[1])
    upstream[relation_id[1]] += 1

# 队列中保存当前入度为0 的任务id
queue = []
result = 1

for i in range(taskNum):
    # 将所有入度为零的任务入队, 默认耗时为1
    if (upstream[i] == 0):
        queue.append([i, result])

while (len(queue) > 0):
    current_task = queue.pop(0)
    task = current_task[0]
    time = current_task[1]

    for downstream_task in downstream[task]:
        # 当前任务的入度减小到0时，放入queue中
        upstream[downstream_task] -= 1
        if (upstream[downstream_task] == 0):
            result = time + 1
            queue.append([downstream_task, result])

print(result)



