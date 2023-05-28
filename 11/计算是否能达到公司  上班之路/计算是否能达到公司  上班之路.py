# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import collections
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 并查集模板
class UF:
    def __init__(self, n=0):
        self.count = n
        self.item = [0 for x in range(n + 1)]
        for i in range(n):
            self.item[i] = i

    def find(self, x):
        if (x != self.item[x]):
            self.item[x] = self.find(self.item[x])
            return 0
        return x

    def union_connect(self, x, y):
        x_item = self.find(x)
        y_item = self.find(y)

        if (x_item != y_item):
            self.item[y_item] = x_item
            self.count -= 1


# 处理输入
directions = [[0, 1, 1], [0, -1, 2], [1, 0, 3], [-1, 0, 4]]

# 处理输入
params = [int(x) for x in input().split(" ")]
t = params[0]
c = params[1]
params1 = [int(x) for x in input().split(" ")]
n = params1[0]
m = params1[1]
matrix = []
for i in range(n):
    matrix.append([x for x in input()])


def dfs(visited, x, y, ut, uc, last_direct):
    global t, c, n, m, directions
    # 找到目的地
    if ('T' == matrix[x][y]):
        return True

    # 表示当前点已走过
    visited[x][y] = True
    # print(visited)
    # 有四个方向选择走下一步
    for direction in directions:

        direct = direction[2]
        new_x = x + direction[0]
        new_y = y + direction[1]
        # 转向+破壁标记
        turn_flag = False
        break_flag = False

        # 越界 + 是否当前点已访问判断
        if (new_x >= 0 and new_x < n and new_y >= 0 and new_y < m and not visited[new_x][new_y]):

            # 转向+破壁判断
            if (last_direct != 0 and last_direct != direct):
                # 转向次数已用尽
                if (ut + 1 > t):
                    continue
                turn_flag = True

            if ('*' == matrix[new_x][new_y]):
                # 破壁次数已用尽
                if (uc + 1 > c):
                    continue
                break_flag = True

            # 可到达目的地T, 返回True
            if (dfs(visited, new_x, new_y, ut + 1 if turn_flag else ut, uc + 1 if break_flag else uc, direct)):
                return True

    return False


flag = True
for i in range(n):
    for j in range(m):
        visited = [[False for y in range(m)] for x in range(n)]
        if ('S' == matrix[i][j]):
            if (dfs(visited, i, j, 0, 0, 0)):
                print("YES")
                flag = False
                break
            else:
                print("NO")
                flag = False
                break
    if (not flag):
        break

if (flag):
    print("NO")