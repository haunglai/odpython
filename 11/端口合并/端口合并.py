import functools


def check(ranges1, ranges2):
    count = 0
    for i in ranges1:
        if i in ranges2:
            count += 1
    if count >= 2:
        return True
    return False


def merge(ranges):
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            if (check(ranges[i], ranges[j])):
                ranges[i] = ranges[i].union(ranges[j])
                ranges.pop(j)
                return True
    return False


# 处理输入
m = int(input())
ranges = []
# 利用set来保存区间，方便判断是否有相交
for i in range(m):
    ranges.append(set([int(x) for x in input().split(",")]))

while (merge(ranges)):
    # print (ranges)
    pass

# 输出的时候要转一下
for i in range(len(ranges)):
    ranges[i] = list(ranges[i])
print(ranges)