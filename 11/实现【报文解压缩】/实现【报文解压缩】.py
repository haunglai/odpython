# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter


def dfs(pos):
    num, char = '', ''
    for pos in range(pos, len(s)):
        if s[pos].isalnum():
            num += s[pos]
        if s[pos] == '[':
            j = pos + 1
            while j < len(s):
                if s[j].isalpha():
                    char += s[j]
                    j += 1
                elif s[j] == ']':
                    return j + 1, char * int(num)
                elif s[j].isalnum():
                    new, sub = dfs(j)
                    j, char = new, char + sub


s = input().strip()
ans, i = '', 0
while True:
    if i >= len(s):
        break
    i, ret = dfs(i)
    ans += ret
print(ans)