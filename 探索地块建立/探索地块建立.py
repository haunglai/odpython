# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import copy


def maxSideLength(mat, threshold, c):
    m, n = len(mat), len(mat[0])
    P = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]

    ans = 0;
    # print (P)
    # 2、遍历前缀和矩阵，获得边长等于c的矩阵
    for i in range(c, m + 1):
        for j in range(c, n + 1):
            # 重点理解：减去点[i-c][j]和点[i][j-c]的矩阵前缀和，剩下来的为一个边长为c正方形，注意点[i-c][j-c]减了两次，需要加一个回来
            if (P[i][j] - P[i - c][j] - P[i][j - c] + P[i - c][j - c] >= threshold):
                ans += 1
    # coding:utf-8
    import functools

    # 处理输入
    count = int(input())
    blocks = {}
    for i in range(count):
        num = int(input())
        if num in blocks:
            blocks[num].append(i)
        else:
            blocks[num] = [i]

    max_distance = -1;
    for block_num in blocks:
        if len(blocks[block_num]) > 1:
            max_distance = max(max_distance, max(blocks[block_num]) - min(blocks[block_num]));

    print(max_distance)
    return ans


# 处理输入
# print ( input())

input_params = [int(x) for x in input().split(" ")]
n = input_params[0]
m = input_params[1]
c = input_params[2]
k = input_params[3]

matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split(" ")])

print(maxSideLength(matrix, k, c))

