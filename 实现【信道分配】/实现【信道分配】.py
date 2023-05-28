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

temp2 = int(input().strip())
r_list = list(map(int, input().strip().split()))
input_temp = int(input().strip())
index = 0
m_number = 0
d_map = {}

while (index < len(r_list)):
    d_map[2 ** index] = r_list[index]
    index = index + 1
for tem in d_map.keys():
    if tem >= input_temp:
        m_number = d_map[tem] + m_number
        d_map[tem] = 0
cint = 0
for j in d_map.keys():
    cint += j * d_map[j]
m_number = int(cint // input_temp) + m_number

print(m_number)