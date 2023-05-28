# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math


def judge(child_num):
    if child_num <= 0 or child_num > 999:
        return False
    return True


childs = input().split()
if len(childs) == 0:
    print("ERROR")
else:
    # 两个班
    class_1, class_2 = list(), list()
    flag = True
    for child in childs:
        if child == childs[0]:
            child_num = int(child.split("/")[0])
            if not judge(child_num):
                print("ERROR")
                break
            class_1.append(child_num)
        else:
            chlid_num, chlid_sign = int(child.split("/")[0]), child.split("/")[1]
            if not judge(chlid_num):
                print("ERROR")
                break
            if chlid_sign == "N":
                flag = not flag
            if flag:
                class_1.append(chlid_num)
            else:
                class_2.append(chlid_num)
    # 排序输出
    class_1.sort()
    class_2.sort()
    if class_1 == [] or class_2 == []:
        class_list = class_1 + class_2
        print(" ".join([str(i) for i in class_list]))
    if class_1[0] <= class_2[0]:
        print(" ".join([str(x) for x in class_1]))
        print(" ".join([str(x) for x in class_2]))
    else:
        print(" ".join([str(x) for x in class_2]))
        print(" ".join([str(x) for x in class_1]))