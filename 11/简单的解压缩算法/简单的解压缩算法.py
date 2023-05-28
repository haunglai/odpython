# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import collections
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 并查集模板
class UF:
    def __init__(self, n=0):
        self.count = n
        self.item = [0 for x in range(n + 1)]
        for i in range(n):
            self.item[i] = i

    def find(self, x):
        if (x != self.item[x]):
            self.item[x] = self.find(self.item[x])
            return 0
        return x

    def union_connect(self, x, y):
        x_item = self.find(x)
        y_item = self.find(y)

        if (x_item != y_item):
            self.item[y_item] = x_item
            self.count -= 1


def repeat_operation(stack, pos, repeat_count):
    count = len(stack) - pos

    # temp_stack用于存储弹栈数据
    temp_stack = [0 for x in range(count)]

    while (count >= 1):
        count -= 1
        temp_stack[count] = stack.pop()

    temp_str = "".join(temp_stack)
    result = ""
    # 重复repeat_count次
    for i in range(repeat_count):
        result += temp_str

    stack.append(result);


# 处理输入
input_str = input()
stack = []
# bracket_pos 保存的是所有花括号出现的位置
bracket_pos = []

for i in range(len(input_str)):
    c = input_str[i]
    # { 字符
    if (c == '{'):
        bracket_pos.append(len(stack))

    # 数字
    if (c >= '0' and c <= '9'):
        repeat_count = int(c + "")
        # 若此时栈顶是 } 字符, 将对应的字母重复repeat_count次
        if (stack[-1] == "}"):
            # 获取上一个{的位置
            pos = bracket_pos.pop()
            # 删除左右{
            stack.pop(pos)
            stack.pop()
            # 重复{之间的字母
            repeat_operation(stack, pos, repeat_count)
        else:
            # 不是 } 字符, 简单重复栈顶字符对应次即可
            repeat_operation(stack, len(stack) - 1, repeat_count)
        continue

    # 其他字符 (字母 + )
    stack.append(c + "")

# 输出
print("".join(stack))