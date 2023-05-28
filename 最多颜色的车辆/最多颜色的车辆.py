# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import copy

# 处理输入
cars = [int(x) for x in input().split(" ")]
window_size = int(input())

car_count = [0, 0, 0]
# 初始化滑动窗口
for i in range(window_size):
    car_count[cars[i]] += 1

# 滑动窗口向前滑
max_res = max(max(car_count[0], car_count[1]), car_count[2])
for i in range(window_size, len(cars)):
    car_count[cars[i]] += 1
    car_count[cars[i - window_size]] -= 1
    max_res = max(max_res, max(max(car_count[0], car_count[1]), car_count[2]))
print(max_res)
