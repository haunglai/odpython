# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import copy

# 保存排列组合字符串
res_str_list = []

# 预设值
num_char_map = {}
num_char_map['0'] = "abc"
num_char_map['1'] = "def"
num_char_map['2'] = "ghi"
num_char_map['3'] = "jkl"
num_char_map['4'] = "mno"
num_char_map['5'] = "pqr"
num_char_map['6'] = "st"
num_char_map['7'] = "uv"
num_char_map['8'] = "wx"
num_char_map['9'] = "yz"


# 递归求排列组合
def dfs(num_str, temp_list, index):
    if (index == len(num_str)):
        res_str_list.append("".join(temp_list))
        return
    temp_list_back_up = copy.copy(temp_list)
    for single_char in num_char_map[num_str[index]]:
        temp_list.append(single_char)
        dfs(num_str, temp_list, index + 1)
        temp_list.pop()


# 处理输入
num_str = input()
block_str = input()
dfs(num_str, [], 0)

# 过滤
for single_str in res_str_list:
    if block_str in single_str:
        res_str_list.remove(single_str)

print(res_str_list)
