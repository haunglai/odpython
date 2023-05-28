# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter

s = input()
s_slices = Counter(s)
num = s_slices.get("o", 0)
print(len(s) - 1 if num % 2 else len(s))