# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]


def bfs(n, m, matrix, flipped):
    global directions
    if (len(flipped) == 0):
        return;

    pos = flipped.pop(0)
    for d in directions:
        newX = pos[0] + d[0]
        newY = pos[1] + d[1]
        if (newX >= 0 and newX < n and
                newY >= 0 and newY < m and
                matrix[newX][newY] == 1):
            matrix[newX][newY] = 0
            flipped.append([newX, newY])

    bfs(n, m, matrix, flipped)


# 处理输入
params = [int(x) for x in input().split(" ")]
n = params[0]
m = params[1]
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split(" ")])

# 起点可以是每一个位置
result = 0;
for i in range(n):
    for j in range(m):
        if (matrix[i][j] == 1):
            result += 1
            flipped = []
            flipped.append([i, j])
            bfs(n, m, matrix, flipped)

print(result)