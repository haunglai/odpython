# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools


def find(n, k):
    if (n == 0):
        return 'R'
    len = pow(2, n)
    # 如果 k 在后半段，则与前一个字符串相同
    if (k >= len / 2):
        pos = k - len / 2
        return find(n - 1, pos)
    else:
        # 如果 k 在前半段，则与前一个字符串相反
        if (find(n - 1, k) == 'R'):
            return 'B'
        else:
            return 'R'


# 处理输入
t = int(input())
input_case = []
for i in range(t):
    input_case.append([int(x) for x in input().split(" ")])

for i in range(t):
    n = input_case[i][0]
    k = input_case[i][1]
    if (find(n - 1, k) == 'R'):
        print("red")
    else:
        print("blue")

