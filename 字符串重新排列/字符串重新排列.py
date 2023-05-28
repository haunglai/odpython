# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

# 处理输入
input_str = input()
input_list = input_str.split(" ")

# 第一步，单词内部调整
new_list = []
for single_str in input_list:
    new_list.append("".join(sorted(single_str, reverse=False)))


# 自定义排序函数，a,b为(str,count)
def comp(a, b):
    if (a[1] > b[1]):
        return -1
    elif (a[1] == b[1]):
        if (len(a[0]) > len(b[0])):
            return 1
        elif (len(a[0]) == len(b[0])):
            if (a[0] > b[0]):
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return 1


# 第二步，单词间调整
# 先统计每个单词出现的次数
str_count = {}
for single_str in new_list:
    if single_str in str_count:
        str_count[single_str] += 1
    else:
        str_count[single_str] = 1
print(str_count)

list1 = sorted(str_count.items(), key=functools.cmp_to_key(comp))

res_str = ""
for item in list1:
    for i in range(item[1]):
        res_str += item[0] + " "
print(res_str)