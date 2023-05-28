# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

# 处理输入
n = int(input())

nums = [int(x) for x in input().split(" ")]

# 计算频度最高的数字
max_count = 0;
num_count = {}
for i in range(n):
    if nums[i] in num_count:
        num_count[nums[i]] = num_count[nums[i]] + 1
    else:
        num_count[nums[i]] = 1

    max_count = max(max_count, num_count[nums[i]])

max_num = set([])
for item in num_count:
    if num_count[item] == max_count:
        max_num.add(item)

# 找到第一次和最后一次出现位置
result = n;
for i in max_num:
    left = 0
    right = n - 1
    while (nums[left] != i):
        left += 1

    while (nums[right] != i):
        right -= 1

    if (left <= right):
        result = min(result, right - left + 1)

print(result)