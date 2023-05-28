# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import collections
import math
from itertools import combinations
from re import match


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 并查集模板
class UF:
    def __init__(self, n=0):
        self.count = n
        self.item = [0 for x in range(n + 1)]
        for i in range(n):
            self.item[i] = i

    def find(self, x):
        if (x != self.item[x]):
            self.item[x] = self.find(self.item[x])
            return 0
        return x

    def union_connect(self, x, y):
        x_item = self.find(x)
        y_item = self.find(y)

        if (x_item != y_item):
            self.item[y_item] = x_item
            self.count -= 1


def comp(a, b):
    if a[0] == b[0]:
        return a[1] - b[1]
    else:
        return a[0] - b[0]


# 处理输入
nums = [int(x) for x in input().split(" ")]

if len(nums) == 1:
    print(0)
else:
    # 左右乘积子数组
    left_result = [1 for x in range(len(nums) + 1)]
    for i in range(1, len(nums) + 1):
        left_result[i] = left_result[i - 1] * nums[i - 1];

    right_result = [1 for x in range(len(nums) + 1)]
    i = len(nums) - 1
    while (i >= 0):
        right_result[i] = right_result[i + 1] * nums[i];
        i -= 1

    # 找相等位置
    flag = 0;
    for i in range(1, len(nums)):
        if (left_result[i] == right_result[i + 1]):
            flag = 1
            print(i)
            break

    # 不存在中心位置
    if (flag == 0):
        print(-1)      