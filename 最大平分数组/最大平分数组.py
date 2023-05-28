# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools


def canPartitionKSubsets(nums, k):
    all = sum(nums)
    if all % k:
        return False
    per = all // k
    nums.sort()
    if nums[-1] > per:
        return False
    n = len(nums)
    dp = [False] * (1 << n)
    dp[0] = True
    cursum = [0] * (1 << n)
    for i in range(0, 1 << n):
        if not dp[i]:
            continue
        for j in range(n):
            if cursum[i] + nums[j] > per:
                break
            if (i >> j & 1) == 0:
                next = i | (1 << j)
                if not dp[next]:
                    cursum[next] = (cursum[i] + nums[j]) % per
                    dp[next] = True
    return dp[(1 << n) - 1]


# 处理输入
n = int(input())
nums = [int(x) for x in input().split(" ")]

for i in reversed(range(n + 1)):
    # 从最大的可能行开始，满足条件即为为最小的情况
    if (canPartitionKSubsets(nums, i)):
        print(i)
        break;