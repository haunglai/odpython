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


def generate(nums):
    res = list()
    for i in nums:
        res.append(i)
        for j in nums:
            if j != i:
                res.append(i * 10 + j)
            for k in nums:
                if len({i, j, k}) == 3:
                    res.append(i * 100 + j * 10 + k)
    return res


def exclude(nums):
    temp = list()
    for i in nums:
        s = list(str(i))
        if ("2" in s and "5" in s) or ("6" in s and "9" in s):
            continue
        else:
            temp.append(i)
    return temp


nums = [int(x) for x in input().split(",")]
n = max(nums)
ans = nums.copy()
if (2 in nums and 5 in nums) or (6 in nums and 9 in nums):
    print(-1)
elif len(set(nums)) == 3:
    print(-1)
else:
    temp = nums.copy()
    ref = {2: 5, 5: 2, 6: 9, 9: 6}
    for key, value in ref.items():
        if key in nums:
            temp.append(value)
    ans = generate(temp)
    ans = exclude(ans)
    ans = list(set(ans))
    idx = min(len(ans), n)
    ans.sort()
    print(ans[idx - 1])