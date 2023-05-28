# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

# 处理输入
inputs = input().split(" ")
char_str = inputs[0]
n = int(inputs[1])

# 将n行格子看作是n个数组
res_array = [[] for i in range(n)]

index = 0
# 控制下一个字符归属到哪个数组
flag = True

for c in char_str:
    if (index == -1):
        index = 0
        flag = True

    if (index == n):
        index = n - 1
        flag = False

    res_array[index].append(c)

    if (flag):
        index += 1
    else:
        index -= 1

for single_array in res_array:
    print("".join(single_array))



