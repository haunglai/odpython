# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math
import sys


def change_order_compare(problem, answer):
    problem_str = ''.join(sorted(problem))
    answer_str = ''.join(sorted(answer))

    if (problem_str == answer_str):
        return True

    return False


def duplicate_compare(problem, answer):
    problem_set = set();
    for c in problem:
        problem_set.add(c)

    answer_set = set();
    for c in answer:
        answer_set.add(c)

    if (answer_set == problem_set):
        return True
    return False


# 处理输入
problems = input().split(",")
answers = input().split(",")

resList = []
for i in range(len(problems)):
    problem = problems[i]
    flag = False
    for j in range(len(answers)):
        answer = answers[j]
        # 变换顺序 + 去重对比
        if (change_order_compare(problem, answer)):
            resList.append(answer)
            flag = True
        elif (duplicate_compare(problem, answer)):
            resList.append(answer)
            flag = True
    if (not flag):
        resList.append("not found");

print(",".join(resList))