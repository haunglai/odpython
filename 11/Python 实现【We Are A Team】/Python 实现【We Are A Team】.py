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

line = input().strip()
values = list(map(int, line.split()))
n = values[0]
m = values[1]
if n < 1 or m > 100000:
    print("NULL")
else:
    l = []
    team = []
    for i in range(m):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        a = values[0]
        b = values[1]
        c = values[2]

        if (a > n or b > n):
            print("da pian zi")
        elif c == 0:
            flag = True
            for i in team:
                if i.count(a) + i.count(b) > 0:
                    flag = False
                    if i.count(a) == 0:
                        i.append(a)
                    else:
                        i.append(b)
            if flag:
                new = []
                new.append(a)
                new.append(b)
                team.append(new)

        elif c == 1:
            flag = False
            for i in team:
                if i.count(a) + i.count(b) > 1:
                    flag = True
            if flag:
                print("we are a team")
            else:
                print("we are not a team")
        else:
            print("da pian zi")