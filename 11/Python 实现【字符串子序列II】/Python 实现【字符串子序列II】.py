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

s1, s2 = input(), input()
idx, ans = 1, -1
i = len(s1) - 1
while i > -1:
    for j in range(len(s2) - idx, -1, -1):
        idx += 1
        if s1[i] == s2[j]:
            if i == 0:
                ans = j
            break
    i -= 1
print(ans)