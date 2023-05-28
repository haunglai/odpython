# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

k = 0


def bfs(matrix, visited, x, y):
    global k
    visited[x][y] = True
    # 四个方向查看是否可行
    for d in direction:
        newX = x + d[0]
        newY = y + d[1]
        if (newX >= 0 and newX < len(matrix) and newY >= 0 and newY < len(matrix[0])):
            if (not visited[newX][newY] and abs(matrix[x][y] - matrix[newX][newY]) <= 1):
                k += 1
                bfs(matrix, visited, newX, newY)


# 处理输入
params = [int(x) for x in input().split(" ")]
X = params[0]
Y = params[1]
matrix = []
for i in range(X):
    matrix.append([int(x) for x in input().split(" ")])

# 起点可以是每一个位置
result = 0;
for i in range(X):
    for j in range(Y):
        visited = [[False for y in range(Y)] for x in range(X)]
        k = 1
        bfs(matrix, visited, i, j)
        result = max(k, result)

print(result)