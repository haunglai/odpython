# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

# 处理输入
items = int(input())
days = int(input())
max_items = [int(x) for x in input().split(" ")]
prices = []
for i in range(items):
    prices.append([int(x) for x in input().split(" ")])
# print (prices)

max_profit = 0;
for i in range(len(prices)):
    ans = 0
    for j in range(1, len(prices[i])):
        ans += max(0, prices[i][j] - prices[i][j - 1]);
    max_profit += ans * max_items[i]

print(max_profit)