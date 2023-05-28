# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import collections
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_shorter_time(a, b):
    if (a * 10 < b):
        return a * 10
    return b


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


def getCount(nums, offset):
    count = 0;
    for num in nums:
        temp = num + offset
        if (temp < 0 or temp > 255):
            count += 1
    return count


def fixOffset(nums, offset, count):
    if (count == 0):
        return offset

    offsetOld = offset
    for num in nums:
        temp = num + offsetOld
        if (temp < 0):
            offset += temp / (len(nums) - count)
        elif (temp > 255):
            offset += (temp - 255) / (len(nums) - count)
    return fixOffset(nums, offset, getCount(nums, offset) - count)


# 处理输入
nums = [int(x) for x in input().split(" ")]

# 计算
offset = 128 - sum(nums) * 1.0 / len(nums)
offset = fixOffset(nums, offset, getCount(nums, offset))
if (offset - math.floor(offset) <= 0.5):
    offset = math.floor(offset)
else:
    offset = math.ceil(offset)
print(int(offset))