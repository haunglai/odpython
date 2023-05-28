# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import collections


def comp(a, b):
    return a - b


def comp1(a, b):
    return a[0] - b[0]


result_machine = 0

# 处理输入
task_num = input()

i = int(task_num)
ranges = []
while (i > 0):
    input_str = input()
    input_list = [int(x) for x in input_str.split(" ")]
    ranges.append(input_list)
    i = i - 1
# 区间排序
ranges = sorted(ranges, key=functools.cmp_to_key(comp1))

points = set()
for single_range in ranges:
    points.add(single_range[0])
    points.add(single_range[1])
# 点排序
points = sorted(points, key=functools.cmp_to_key(comp))

result = 0;
ignore = set()

for point in points:
    current_sum = 0
    for i in range(len(ranges)):
        if (i in ignore):
            continue

        start = ranges[i][0]
        end = ranges[i][1]
        count = ranges[i][2]

        if (point < start):
            break
        elif (point < end):
            current_sum += count
        else:
            ignore.add(i)

    result = max(result, current_sum)

print(result)