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


def maxArea(height):
    left = -1
    right = -1
    l, r = 0, len(height) - 1
    ans = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        if area > ans:
            left = l
            right = r
            ans = area

        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return [ans, left, right]


heights = [int(x) for x in input().split(" ")]
result = maxArea(heights)
print(result[0])
print(result[1], end=' ')
print(result[2])
