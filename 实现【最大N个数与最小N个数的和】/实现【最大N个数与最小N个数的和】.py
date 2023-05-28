# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter

m = int(input())
nums = sorted(list(set(map(int, input().split()))))
n = int(input())
if len(nums) < 2 * n or nums[0] < 0 or nums[-1] > 1000:
    print(-1)
else:
    min_nums, max_nums = nums[:n], nums[-n:]
    result = sum(min_nums) + sum(max_nums) if not set(min_nums) & set(max_nums) else -1
    print(result)