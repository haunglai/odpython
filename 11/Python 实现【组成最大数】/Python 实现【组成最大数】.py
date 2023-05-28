# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy


def compare(a, b):
    return 1 if int(a + b) < int(b + a) else -1


num_list = sorted(input().split(","), key=functools.cmp_to_key(compare))
print("".join(num_list))