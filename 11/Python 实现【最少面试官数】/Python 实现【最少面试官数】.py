# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys


def is_vaild(hr, plan):
    def compare(ls1, ls2):
        a, b = ls1[0], ls1[1]
        c, d = ls2[0], ls2[1]
        return a < c < b or a < d < b or (a >= c and b <= d)

    for single_hr in hr:
        if compare(single_hr, plan) or compare(plan, single_hr):
            return False
    return True


def get_ans(plan):
    for hr in hrs:
        if len(hr) >= m:
            continue
        if is_vaild(hr, plan):
            hr.append(plan)
            return True


m, n = int(input()), int(input())
plans = sorted([[int(i) for i in input().split()] for _ in range(n)], key=lambda x: x[0])
hrs = []
for plan in plans:
    if not get_ans(plan):
        hrs.append([plan])
print(len(hrs))