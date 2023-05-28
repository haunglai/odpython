# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools


def comp(a, b):
    return b - a


# 处理输入
params = [int(x) for x in input().split(" ")]
m = params[0]
n = params[1]
matrix = [int(x) for x in input().split(" ")]
target_params = [int(x) for x in input().split(" ")]
target_i = target_params[0]
target_j = target_params[1]
# print(matrix)

# 队列中保存所有大于等于 1 的信号位置
queue = []
# 找到信号源
for i in range(m):
    for j in range(n):
        if (matrix[i * n + j] > 0):
            queue.append([i, j])
            break
# print(queue)

# 信号可以上下左右传播
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while (len(queue) > 0):
    pos = queue[0]
    queue.pop(0)
    i = pos[0]
    j = pos[1]

    # 信号强度为1，则不需要再传播了，后面肯定都是0
    if (matrix[i * n + j] - 1 == 0):
        break

    for direction in directions:
        new_x = i + direction[0];
        new_y = j + direction[1];

        if (new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and matrix[new_x * n + new_y] == 0):
            matrix[new_x * n + new_y] = matrix[i * n + j] - 1
            queue.append([new_x, new_y])

print(matrix[target_i * n + target_j])