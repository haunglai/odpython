# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re
import math


def judge(max_num, num_count):
    ret = True
    for i in num_count:
        if 0 < num_count[i] and i != max_num:
            pair_num = max_num - i
            if pair_num == i:
                if num_count[i] % 2 != 0:
                    ret = False
                    break
            elif num_count[pair_num] != num_count[i]:
                ret = False
                break
    return ret


nums = list(map(int, input().split()))
total_sum, max_num = sum(nums), max(nums)
num_count = Counter(nums)
max_height = -1
for i in range(total_sum // max_num, 0, -1):
    if total_sum % i == 0:
        num = total_sum // i
        if num <= max_num * 2:
            if judge(total_sum // i, num_count) and max_height < i:
                max_height = i
print(max_height)