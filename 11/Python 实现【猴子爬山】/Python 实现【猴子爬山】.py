# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

input_str = int(input())
nums = [1, 1, 2]
while len(nums) < input_str + 1:
    nums.append(nums[-1] + nums[-3])

print(nums[input_str - 1])