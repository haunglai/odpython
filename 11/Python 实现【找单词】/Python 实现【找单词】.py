# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re


def get_res(matrix, word):
    m, n, w = len(matrix), len(matrix[0]), len(word)

    def dfs(i, j, k):
        if not 0 <= i < m or not 0 <= j < n or matrix[i][j] != word[k]:
            return False
        if k == w - 1:
            path.append((i, j))
            ans = list()
            for a, b in path:
                ans.extend([str(a), str(b)])
            print(",".join(ans))
            return True
        matrix[i][j] = ""
        path.append((i, j))
        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)
        matrix[i][j] = word[k]
        path.remove((i, j))
        return res

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False


row = int(input())
matrix = [input().split(",") for _ in range(row)]
word = input()
path = list()
if not get_res(matrix, word):
    print("N")