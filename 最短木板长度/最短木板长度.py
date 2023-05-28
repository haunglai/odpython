# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

# 处理输入
params = [int(x) for x in input().split(" ")]
n = params[0]
m = params[1]
woods = [int(x) for x in input().split(" ")]

woods = sorted(woods)
result = 0;

# 遍历给的木料长度，每次都补一下最短的木板，每次补完之后重新排序，重复此步骤。
for i in range(m):
    woods[0] = woods[0] + 1
    woods = sorted(woods)
    result = max(result, woods[0])

print(result)



