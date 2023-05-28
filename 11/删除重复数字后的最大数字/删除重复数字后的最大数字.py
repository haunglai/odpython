# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools


def get_max_number(nums):
    # 统计出现次数 + 已经使用的次数
    cnt = {}
    st_cnt = {}
    for v in nums:
        if v in cnt:
            cnt[v] += 1
        else:
            cnt[v] = 1
    # 栈
    res = []
    res.append(-1)
    for x in nums:
        # 已经使用2次，直接跳过
        if (x in st_cnt and st_cnt[x] == 2):
            cnt[x] -= 1
            continue

        # 当前数字大于栈尾数字，且栈尾数字出现超过2次
        while (x > res[-1] and res[-1] in cnt and cnt[res[-1]] > 2):
            cnt[res[-1]] -= 1
            st_cnt[res[-1]] -= 1
            res.pop()

        res.append(x)
        if x in st_cnt:
            st_cnt[x] += 1
        else:
            st_cnt[x] = 1

    for x in res:
        if x != -1:
            print(x, end="")


# 处理输入
nums = [int(x) for x in input()]
get_max_number(nums)


