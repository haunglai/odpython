# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re
import math

input_ops = input().split("#")
res = input_ops[0]
if "$" in res:
    ret = res.split("$")
    res = ret[0]
    for num in ret[1:]:
        res = 3 * int(res) + int(num) + 2
else:
    res = int(res)

for i in range(1, len(input_ops)):
    if "$" in input_ops[i]:
        num_list = input_ops[i].split("$")
        temp = num_list[0]
        for num in num_list[1:]:
            temp = 3 * int(temp) + int(num) + 2
        res = 2 * int(res) + 3 * int(temp) + 4
    else:
        res = 2 * int(res) + 3 * int(input_ops[i]) + 4

print(res)