# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

# 处理输入
n = int(input())
nums = [int(x) for x in input().split(" ")]

res = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] ^ nums[j] > nums[i] & nums[j]:
            res += 1

print(res)