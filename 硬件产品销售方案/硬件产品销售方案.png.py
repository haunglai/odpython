# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import collections


def combinationSum(candidates, target):
    def dfs(candidates, begin, size, path, res, target):
        if target == 0:
            res.append(path)
            return

        for index in range(begin, size):
            residue = target - candidates[index]
            if residue < 0:
                break

            dfs(candidates, index, size, path + [candidates[index]], res, residue)

    size = len(candidates)
    if size == 0:
        return []
    candidates.sort()
    path = []
    res = []
    dfs(candidates, 0, size, path, res, target)
    return res


# 处理输入
amount = int(input())
products = [int(x) for x in input().split(",")]

print(combinationSum(products, amount))