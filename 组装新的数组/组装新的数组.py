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
nums = [int(x) for x in input().split(" ")]
m = int(input())
# 排序找到最小值
nums = sorted(nums)
min_num = nums[0]


def dfs(nums, index, num_sum, count):
    if (num_sum > m):
        return count
    # 满足边界条件+1
    if (num_sum <= m and m - min_num < num_sum):
        return count + 1

    for i in range(index, len(nums)):
        count = dfs(nums, i, num_sum + nums[i], count)

    return count


print(dfs(nums, 0, 0, 0))




