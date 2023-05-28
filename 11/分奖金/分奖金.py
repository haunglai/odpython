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


def monoStack(nums):
    n = len(nums)
    res = [-1] * n
    stack = list()
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack[-1]] = (nums[i] - nums[stack[-1]]) * (i - stack[-1])
            stack.pop()
        stack.append(i)
    return res


# 处理输入
N = int(input())
nums = [int(x) for x in input().split(" ")]

res = monoStack(nums)
for i in range(len(res)):
    if res[i] == -1:
        res[i] = nums[i]
print(res)