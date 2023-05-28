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

nums = [int(x) for x in input().split(",")]

aTime = nums[0]
bTime = nums[1]
num = nums[2]

total = set()
for i in range(len(nums) + 1):
    res = aTime * (num - i) + i * bTime
    total.add(res)

print(sorted(list(total)))
