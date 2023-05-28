# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re
import math

n = int(input())
nums = list(map(int, input().split()))
start = nums[0]
for i in range(1, n):
    start ^= nums[i]
if start != 0:
    print(-1)
else:
    print(sum(nums) - min(nums))