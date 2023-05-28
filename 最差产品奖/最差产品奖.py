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
N = int(input())
nums = [int(x) for x in input().split(",")]

res = ""
dq = []
for i in range(len(nums)):
    if (i >= N):
        # 输出单调队列队首元素，该元素即为移动前滑动窗口的最小值
        res += str(dq[0]) + ","
        # 如果移动到当前滑动窗口位置后，出去的元素恰好是单调队列最小元素，则出队它
        if (nums[i - N] == dq[0]):
            dq.pop(0);

    # 队列不为空且队列中最后的元素大于当前元素
    # 将队列最后元素出队
    # 因为它不可能成为最小元素了
    while (len(dq) > 0 and dq[-1] > nums[i]):
        dq.pop(len(dq) - 1)

    # 当前元素入队
    dq.append(nums[i])

res += str(dq[0])

print(res)
