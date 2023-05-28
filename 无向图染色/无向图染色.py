# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

# 处理输入
input_param = [int(x) for x in input().split(" ")]
m = input_param[0]
n = input_param[1]

# 构造边的数据结构
edges = []
for i in range(n):
    edges.append([int(x) for x in input().split(" ")])

count = 0
for i in range((1 << m)):
    flag = True;
    for j in range(n):
        # 检测所有的边相连的是否同为红颜色
        if ((i >> (m - edges[j][0]) & 1) == 1 and (i >> (m - edges[j][1]) & 1) == 1):
            flag = False
            break

    if flag:
        count += 1

print(count)