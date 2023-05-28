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


def comp(a, b):
    if (a[1] == b[1]):
        if (a[2] == b[2]):
            return a[0] - b[0]
        else:
            return a[2] - b[2]
    else:
        return b[1] - a[1]


# 新员工数量
n = int(input())
# 每天打卡的员工数量
employee_count = [int(x) for x in input().split(" ")]
# 打卡记录
employee_ids = []
for i in range(30):
    employee_ids.append([int(x) for x in input().split(" ")])

# key为员工ID， value为其打卡的记录信息：[打卡次数，首次打卡index]
employee_info = {}
for i in range(30):
    for j in employee_ids[i]:
        if (j in employee_info):
            employee_info[j][0] += 1
        else:
            employee_info[j] = [1, i]

# 将map信息转到list中，以便后续排序
employee_list = []
for key in employee_info:
    employee_list.append([key, employee_info[key][0], employee_info[key][1]]);

employee_list = sorted(employee_list, key=functools.cmp_to_key(comp));

res = []
for i in range(5):
    res.append(str(employee_list[i][0]))

# 输出
print(" ".join(res))
