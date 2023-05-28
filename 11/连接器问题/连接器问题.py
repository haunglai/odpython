# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools


def comp(a, b):
    if a[0] == b[0]:
        return a[1] - b[1]
    else:
        return a[0] - b[0]


# 处理输入
input_ranges = [int(x) for x in input().replace("[", "").replace("]", "").split(",")]
input_connectors = [int(x) for x in input().replace("[", "").replace("]", "").split(",")]

# print (input_ranges)
ranges = []
for i in range(len(input_ranges)):
    if i % 2 != 0:
        ranges.append([input_ranges[i - 1], input_ranges[i]])

ranges = sorted(ranges, key=functools.cmp_to_key(comp))

# print (ranges)


result = 0
distances = []
left = ranges[0][0]
right = ranges[0][1]
for i in range(len(ranges)):
    if (ranges[i][0] <= right):
        right = max(right, ranges[i][1])
    else:
        result += 1
        distances.append(ranges[i][0] - right)
        right = ranges[i][1]
result += 1

distances = sorted(distances)
connectors = sorted(input_connectors)

idx = 0;
for i in range(len(connectors)):
    if idx > len(distances):
        break
    if (connectors[i] >= distances[idx]):
        idx += 1
        result -= 1
print(result)