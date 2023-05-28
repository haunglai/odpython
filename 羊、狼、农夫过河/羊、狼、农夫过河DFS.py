# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import copy

# 处理输入
input_nums = [int(x) for x in input().split(" ")]
M = input_nums[0]
N = input_nums[1]
X = input_nums[2]

min_times = (M + N) * X;


# m0, n0 分别表示剩余的羊、狼个数， x为船容量
# m1, n1 分别表示运输到对岸的羊、狼个数，times为次数
def transport(m0, n0, x, m1, n1, times):
    global min_times
    # 若可以一次性运走，结束了，注意等于号。。。
    if (x >= m0 + n0):
        if (times + 1 < min_times):
            min_times = times + 1
        return times + 1

    # 尝试运一部分狼一部分羊
    # 要上船的羊数量不可以超过岸上数量、也不可以超过船的容量
    for i in range(m0):
        if i > x:
            break
        # 要上船的狼的数量不可以超过岸上数量、也不可以超过船装了羊后的剩余的容量
        for j in range(n0):
            if i + j > x:
                break
            # 不可以不运
            if (i + j == 0):
                continue

            # 船离岸后，原来这岸，要么没有羊，要么羊比狼多，才可以运；对岸也要检查，不考虑回程带动物
            if ((m0 - i == 0 or m0 - i > n0 - j) and (m1 + i == 0 or m1 + i > n1 + j)):
                # 运一次
                result = transport(m0 - i, n0 - j, x, m1 + i, n1 + j, times + 1)
                # 如果获取了结果，和minTime比较，但是不结束，继续检查
                if (result < min_times and result != 0):
                    min_times = result

    # 没有方案了。。返回0
    return 0


# 表示已运输到对岸的羊、狼个数
m_temp = 0;
n_temp = 0;

transport(M, N, X, m_temp, n_temp, 0);

if (min_times == (M + N) * X):
    print(0)
else:
    print(min_times)


