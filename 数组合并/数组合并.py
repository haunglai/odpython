# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

# 处理输入
m = int(input())
n = int(input())
num_arrays = []
for i in range(n):
    num_arrays.append([int(x) for x in input().split(',')])

output_str = ""

index = 0
while (len(num_arrays) > 0):
    num_array = num_arrays[index]
    for i in range(m):
        if (len(num_array) == 0):
            num_arrays.pop(index)
            index -= 1
            break
        output_str += str(num_array.pop(0)) + ","

    index += 1
    if (index >= len(num_arrays)):
        index = 0;

print(output_str[:len(output_str) - 1])




