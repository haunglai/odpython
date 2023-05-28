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


def removeIntersect(input_list):
    res = 0
    for i in range(len(input_list)):
        tempList = []
        tempList.append(input_list[i])
        right = input_list[i][1]  # 第一个序列的最后一个元素下标
        for j in range(len(input_list)):
            if (i != j):
                left = input_list[j][0];
                if (left > right):
                    tempList.append(input_list[j])
                    right = input_list[j][1]
        res = max(res, len(tempList));

    return res


# 处理输入
N = int(input())
nums = [int(x) for x in input().split(" ")]

map_info = {}
# 两个for循环遍历所有的连续子数组
for i in range(N):
    count = nums[i]
    for j in range(i, N):
        temp = [i, j]  # 首坐标i，尾座标j
        if (i != j):
            count += nums[j]

        if (count in map_info):
            map_info[count].append(temp)
        else:
            map_info[count] = []
            map_info[count].append(temp)

res = 0
for key in map_info:
    res = max(res, removeIntersect(map_info[key]))

print(res)
