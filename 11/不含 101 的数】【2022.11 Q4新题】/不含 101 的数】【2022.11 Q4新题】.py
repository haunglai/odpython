# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import copy

# 处理输入
nums = input().split(" ")
left = int(nums[0])
right = int(nums[1])

count = right - left + 1
for i in range(left, right + 1):
    bin_str = str(bin(i))
    if '101' in bin_str:
        count -= 1
print(count)
