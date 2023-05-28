# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys

dice = ['1', '2', '3', '4', '5', '6']

s = input()
for i in s:
    if i == 'L':
        uu = [dice[0], dice[4], dice[1], dice[5]]
        dice[0] = uu[1]
        dice[4] = uu[2]
        dice[1] = uu[3]
        dice[5] = uu[0]
    elif i == 'R':
        uu = [dice[0], dice[4], dice[1], dice[5]]
        dice[0] = uu[3]
        dice[4] = uu[0]
        dice[1] = uu[1]
        dice[5] = uu[2]
    elif i == 'F':
        uu = [dice[2], dice[4], dice[3], dice[5]]
        dice[2] = uu[1]
        dice[4] = uu[2]
        dice[3] = uu[3]
        dice[5] = uu[0]
    elif i == 'B':
        uu = [dice[2], dice[4], dice[3], dice[5]]
        dice[2] = uu[3]
        dice[4] = uu[0]
        dice[3] = uu[1]
        dice[5] = uu[2]
    elif i == 'A':
        uu = [dice[0], dice[2], dice[1], dice[3]]
        dice[0] = uu[3]
        dice[2] = uu[0]
        dice[1] = uu[1]
        dice[3] = uu[2]
    elif i == 'C':
        uu = [dice[0], dice[2], dice[1], dice[3]]
        dice[0] = uu[1]
        dice[2] = uu[2]
        dice[1] = uu[3]
        dice[3] = uu[0]

print(''.join(dice))