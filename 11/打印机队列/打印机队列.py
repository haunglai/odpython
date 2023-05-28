# coding:utf-8
import functools


def comp(a, b):
    if a[0] == b[0]:
        return b[1] - a[1]
    else:
        return b[0] - a[0]


# 处理输入
count = int(input())
print_machines = []
for i in range(6):
    print_machines.append([])

file_count = 0
for i in range(count):
    input_info = input().split(" ")
    if input_info[0] == "IN":
        file_count += 1
        print_machines[int(input_info[1])].append((int(input_info[2]), file_count))
    else:
        # 排序
        for i in range(6):
            print_machines[i] = sorted(print_machines[i], key=functools.cmp_to_key(comp))
        if len(print_machines[int(input_info[1])]) > 0:
            print(print_machines[int(input_info[1])][0][1])
            print_machines[int(input_info[1])] = print_machines[int(input_info[1])][1:]
        else:
            print("NULL")

