# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools


def get_char_count(input_str):
    char_count_dict = {}
    for i in input_str:
        if i in char_count_dict:
            char_count_dict[i] += 1
        else:
            char_count_dict[i] = 1
    return char_count_dict


# 处理输入
s1 = input()
s2 = input()
k = int(input())

# 长度限制，不可能存在覆盖子串
if (len(s2) < len(s1) + k):
    print(-1)
else:
    s1_char_count = get_char_count(s1)
    flag = True
    for i in range(len(s2) - len(s1) - k):
        # 子串的字符出现频率统计
        sub_str_char_count = get_char_count(s2[i: i + len(s1) + k])
        for key in s1_char_count:
            if key not in sub_str_char_count:
                flag = False
                break
            if s1_char_count[key] > sub_str_char_count[key]:
                flag = False
                break

        if (flag):
            # 输出索引
            print(i)
            break
    if (flag == False):
        print(-1)


