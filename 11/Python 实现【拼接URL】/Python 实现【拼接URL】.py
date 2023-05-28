# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter
import copy
from itertools import permutations
import re


def get_url(urls):
    result = '/'
    if ',' in urls:
        rep = '/'
        result = re.sub(r'(/+)', rep, urls.replace(',', rep))
    return result


print(get_url(input().strip()))