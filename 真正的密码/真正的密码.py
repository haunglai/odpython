# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import copy

# 处理输入
input_strs = input().split(" ")
# 将所有字符串放入哈希集合
word_set = set()
for single_str in input_strs:
    word_set.add(single_str)
# 真正的密码
true_pass_word = "";

# 按顺序检查每一个词
for single_str in input_strs:
    # 条件1：检查这个词所有以索引0开头的子串在数组中是否都有
    flag = True
    for i in range(1, len(single_str)):
        # 以索引0开头的子串
        sub_str = single_str[0:i]
        if sub_str not in word_set:
            flag = False
            break

    if (flag):
        # 条件2：比较密码长度
        if (len(single_str) > len(true_pass_word)):
            true_pass_word = single_str
        # 条件3：比较密码字典排序
        if (len(single_str) == len(true_pass_word) and single_str > true_pass_word):
            true_pass_word = single_str

print(true_pass_word)