# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re

n = input()
nums = list(map(int, input().split()))
nums.sort()
N = 0

while (len(nums) > 1):
    fisrt_array = nums[0]
    for clo in nums[1:]:
        if (clo % nums[0] == 0):
            nums.remove(clo)
    nums.remove(nums[0])
    N += 1

if (nums):
    print(N + 1)
else:
    print(N)