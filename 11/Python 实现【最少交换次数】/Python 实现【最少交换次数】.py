# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re
import math

nums = input().strip().split()
k = int(input())
list_index, window = [], []
for i in range(len(nums)):
    window.append(i)
    if int(nums[i]) < k:
        list_index.append(i)

len_num = len(list_index)
max_num = 0
for index in list_index:
    num = len(set(list_index) & set(window[index:index + len_num]))
    if num > max_num:
        max_num = num
min = len_num - max_num

print(min)