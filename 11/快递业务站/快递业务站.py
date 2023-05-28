# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

n = int(input())
sites = []
for i in range(n):
    sites.append([int(x) for x in input().split(" ")])

count = 0
# 保存站点覆盖情况
cover = set([])
for i in range(n):
    # 第i个站点未覆盖
    if i not in cover:
        count += 1

    # 第i个站点与其他站点的相连情况
    site = sites[i];
    for j in range(len(site)):
        if (site[j] == 1):
            cover.add(j)
print(count)

