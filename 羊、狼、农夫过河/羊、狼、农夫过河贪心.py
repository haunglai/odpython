# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math
import sys


def comp(a, b):
    return int(a[1]) - int(b[1])


# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import copy

# 处理输入
input_nums = [int(x) for x in input().split(" ")]
M = input_nums[0]
N = input_nums[1]
X = input_nums[2]

# 分支1.1
if (M <= N):
    print(0)
# 分支2.1
elif (N < X):
    # 分支2.1.1
    if (N < math.floor(X / 2)):
        M -= X - N

    print(int(math.ceil(M / X)) + 1)
else:
    # 分支2.2
    N -= X - 1
    N_opposite = X - 1
    M -= X
    M_opposite = X

    # 第一轮已经两次了
    result = 2

    # 后续运输的初始规则（船上的羊多于狼1个）
    if X % 2 == 0:
        sheep_boat = int(math.ceil(X / 2)) + 1
    else:
        sheep_boat = int(math.ceil(X / 2))
    wolf_boat = X - sheep_boat

    # 无解标记
    flag = False
    while (M > 0):
        # 分支2.2.1
        if (M - sheep_boat > N - wolf_boat or (M == sheep_boat and N == wolf_boat)):
            M -= sheep_boat
            M_opposite += sheep_boat
            N -= wolf_boat
            N_opposite += wolf_boat
            result += 1
        # 分支2.2.2
        else:
            tmp = M_opposite - N_opposite - 1
            if (tmp == 0):
                print(0)
                flag = True
                break

            N -= tmp
            N_opposite += tmp
            result += 1
    if not flag:
        print(result)