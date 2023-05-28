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
s = nums[0]
t = nums[1]
a = nums[2]
b = nums[3]

res = 0
add = s
sub = s
while (True):
    if ((t - add) % b == 0):
        break;

    if ((t - sub) % b == 0):
        break;

    add += a
    sub -= a
    res += 1

print(res)