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


def judge(book_i, book_j):
    return book_i[0] < book_j[0] and book_i[1] < book_j[1]


books = sorted(list(eval(input())), reverse=True)
books_num = len(books)
result = [1 for _ in range(books_num)]
for i in range(1, books_num):
    j = 0
    while j < i:
        if judge(books[i], books[j]) and result[i] < result[j] + 1:
            result[i] = result[j] + 1
        j += 1
print(max(result))   