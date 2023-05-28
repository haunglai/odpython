# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools


def cal_time(start, point):
    time = 0
    # 路程时间
    time += point[1] * 10;
    # 去除路程中的排队人数
    point[2] = max(0, point[2] - point[1] * 10);
    # 到监测点的时间
    arrive_time = start + point[1] * 10;
    # 到达时间的分支条件
    if (arrive_time <= 480):
        return 480 - start
    elif (arrive_time <= 600):
        point[2] += (arrive_time - 480) * 3 - (arrive_time - 480)
        return time + point[2]
    elif (arrive_time <= 720):
        return time + point[2]
    elif (arrive_time <= 840):
        point[2] += (arrive_time - 720) * 10 - (arrive_time - 720);
        return time + point[2]
    else:
        return time + point[2]


def comp(a, b):
    if a[4] == b[4]:
        return b[3] - a[3]
    else:
        return a[4] - b[4]


# 处理输入
# 先将时间转换为分钟数
params1 = [int(x) for x in input().split(" ")]
start = params1[0] * 60 + params1[1]
params2 = [int(x) for x in input().split(" ")]
end = params2[0] * 60 + params2[1]
n = int(input())

# 保存核酸点信息
points = []
for i in range(n):
    # 分别为id/距离/排队人数
    point = [int(x) for x in input().split(" ")]
    # 再计算花费和总时间开销
    point.append(point[1] * 10)
    point.append(cal_time(start, point))
    points.append(point)
# print (points)
# 按照排序规则进行排序
points = sorted(points, key=functools.cmp_to_key(comp))

# 过滤不满足时间条件的
res = []
for i in range(len(points)):
    if start + points[i][4] < end:
        res.append(points[i])

# 输出结果
print(len(res))
for point in res:
    print(str(point[0]) + " " + str(point[4]) + " " + str(point[3]))



