# coding:utf-8
import functools


def comp(a, b):
    if a[0] == b[0]:
        return b[1] - a[1]
    else:
        return b[0] - a[0]


# 处理输入
logs = [int(x) for x in input().split(" ")]
# 记录到当前秒的总条数
result = 0

# 记录到当前秒之前的总条数
# 每一轮都会减一次
pre_sum = 0;

# 记录到当前秒首次上报要减去的分数
n_score = 0;

# 记录到首次上报的最大得分
max_score = 0;
for i in range(len(logs)):
    pre_sum = result
    result += logs[i]
    # 还有个100条的限制
    if (result >= 100):
        result = 100
        n_score += pre_sum
        max_score = max(max_score, result - n_score)
        break
    n_score += pre_sum
    max_score = max(max_score, result - n_score)

print(max_score)
