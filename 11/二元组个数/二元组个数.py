# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

# 处理输入
m = int(input())
nums_m = [int(x) for x in input().split(" ")]
n = int(input())
nums_n = [int(x) for x in input().split(" ")]

dict_m = {}
for i in range(m):
    if nums_m[i] in dict_m:
        dict_m[nums_m[i]] += 1
    else:
        dict_m[nums_m[i]] = 1

dict_n = {}
for i in range(n):
    if nums_n[i] in dict_n:
        dict_n[nums_n[i]] += 1
    else:
        dict_n[nums_n[i]] = 1

result = 0
for item_key in dict_m:
    if item_key in dict_n:
        result += dict_m[item_key] * dict_n[item_key]

print(result)