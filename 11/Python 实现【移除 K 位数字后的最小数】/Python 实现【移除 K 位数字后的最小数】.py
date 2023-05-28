# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy


def get_result(num1, num2):
    res_list, count, i = list(), 0, 0
    while i < len(num1):
        count = i
        while res_list and int(res_list[-1]) > int(num1[i]) and num2 != 0:
            res_list.pop()
            num2 -= 1
        res_list.append(num1[i])
        if num2 == 0:
            break
        i += 1
    res_list += num1[count + 1:]
    if num2 > 0:
        res_list = res_list[: len(res_list) - num2]
    return res_list


num1, num2 = list(input()), int(input())
result = "".join(get_result(num1, num2)).lstrip("0")
print(result if result else "0")