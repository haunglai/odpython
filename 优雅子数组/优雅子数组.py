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


def query(left, right, threshold, arr):
    obj = Counter(arr[left:right + 1])
    for cur, count in obj.items():
        if count >= threshold:
            return cur
    return -1


# 处理输入
params = [int(x) for x in input().split(" ")]
k = params[1]
nums = [int(x) for x in input().split(" ")]

res = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if query(i, j, k, nums) != -1:
            res += 1
print(res)