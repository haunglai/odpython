# coding:utf-8
import functools

# 处理输入
count = int(input())
blocks = {}
for i in range(count):
    num = int(input())
    if num in blocks:
        blocks[num].append(i)
    else:
        blocks[num] = [i]

max_distance = -1;
for block_num in blocks:
    if len(blocks[block_num]) > 1:
        max_distance = max(max_distance, max(blocks[block_num]) - min(blocks[block_num]));

print(max_distance)