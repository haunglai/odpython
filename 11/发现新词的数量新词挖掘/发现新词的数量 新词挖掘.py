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


def contin(content, word):
    if (len(content) < len(word)):
        return 0
    if (len(word) == 0):
        return 0
    content_map = {}
    word_map = {}
    # 先统计出word中的字符组成
    for ch in word:
        if ch in word_map:
            word_map[ch] += 1
        else:
            word_map[ch] = 1

    word_char_kind = len(word_map.keys())
    right = 0
    content_child_char_kind = 0
    result = 0
    while (right < len(content)):
        if (right >= len(word)):
            left = right - len(word)
            if content[left] in word_map and content_map[content[left]] == word_map[content[left]]:
                content_child_char_kind -= 1
            content_map[content[left]] -= 1
        if content[right] in content_map:
            content_map[content[right]] += 1
        else:
            content_map[content[right]] = 1

        if content[right] in word_map and content_map[content[right]] == word_map[content[right]]:
            content_child_char_kind += 1
        right += 1
        if (content_child_char_kind == word_char_kind):
            result += 1

    return result


# 处理输入
content = input()
word = input()

print(contin(content, word))




