# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools


def find_min_line(ranges, index, ans, start, min_num, total_length):
    # 完全覆盖
    if (ranges[index][1] - start >= total_length):
        min_num = min(min_num, ans)
        return

    temp = 0;
    for i in range(index + 1, len(ranges)):
        # 找出剩余线段中坐端点小于起始线段的右端点
        if (ranges[i][0] <= ranges[index][1]):
            if (ranges[i][1] > ranges[temp][1]):
                temp = i;
        else:
            break
        if (temp != 0):
            find_min_line(ranges, temp, ans + 1, start, min_num, total_length);


def comp(a, b):
    if a[0] == b[0]:
        return b[1] - a[1]
    else:
        return b[0] - a[0]


# 处理输入
m = int(input())
ranges = []
for i in range(m):
    ranges.append([int(x) for x in input().split(",")])

sorted(ranges, key=functools.cmp_to_key(comp))

total_length = ranges[len(ranges) - 1][1] - ranges[0][0]

# 区间起点
start = 0
min_num = len(ranges)
for i in range(m):
    start = ranges[i][0];
    find_min_line(ranges, i, 1, start, min_num, total_length)

print(min_num)