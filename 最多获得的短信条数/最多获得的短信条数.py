# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools


def comp(a, b):
    return b[2] - a[2]


# 处理输入
money = int(input())
topup_info = [int(x) for x in input().split(" ")]

topup_details = []
for i in range(len(topup_info)):
    topup_detail = []
    topup_detail.append(i + 1)
    topup_detail.append(topup_info[i])
    topup_detail.append(topup_info[i] / (i + 1))
    topup_details.append(topup_detail)

# 按照一块钱最多能买多少条短信排序
topup_details = sorted(topup_details, key=functools.cmp_to_key(comp))
# print(topup_details)
# 贪心选择

result = 0;
i = 0
while (money > 0):
    if (topup_details[i][0] <= money):
        result += topup_details[i][1]
        money -= topup_details[i][0]
    if (i == len(topup_details) - 1):
        i = 0
    i += 1;
print(result)



