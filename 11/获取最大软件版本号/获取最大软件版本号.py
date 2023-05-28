# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy


def comp(a, b):
    if (a[0] == b[0]):
        if (a[1] == b[1]):
            if (a[2] == b[2]):
                return a[3] > b[3]
            else:
                return a[2] > b[2]
        else:
            return a[1] > b[1]
    else:
        return a[0] > b[0]


# 处理输入
version1 = input().split("-")
verson1_no = version1[0].split(".")
verson1_no.append(version1[1])

version2 = input().split("-")
verson2_no = version2[0].split(".")
verson2_no.append(version2[1])

if (comp(verson1_no, verson2_no)):
    print("-".join(version1))
else:
    print("-".join(version2))
