# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math


def cal(flaw, src):
    res = 0
    for i in range(len(src)):
        count = 0
        if src[i] not in "aeiouAEIOU":
            continue
        for j in range(i + 1, len(src)):
            if src[j] not in "aeiouAEIOU":
                count += 1
            else:
                if count > flaw:
                    break
                if count == flaw and res < j - i + 1:
                    res = j - i + 1
    return res


flaw = int(input())
src = input()
count = 0
for i in src:
    if i in "aeiouAEIOU":
        count += 1
if flaw == 0 and count == 1:
    print(1)
else:
    res = cal(flaw, src)
    print(res)
