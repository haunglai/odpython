# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter

str_1 = input()
str_2 = input()
if str_2 not in str_1:
    print("No")
else:
    print(str_1.index(str_2) + 1)
