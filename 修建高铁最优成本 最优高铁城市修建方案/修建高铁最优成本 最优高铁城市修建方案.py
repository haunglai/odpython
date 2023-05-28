# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_shorter_time(a, b):
    if (a * 10 < b):
        return a * 10
    return b


# 并查集模板
class UF:
    def __init__(self, n=0):
        self.count = n
        self.item = [0 for x in range(n + 1)]
        for i in range(n):
            self.item[i] = i

    def find(self, x):
        if (x != self.item[x]):
            self.item[x] = self.find(self.item[x])
            return 0
        return x

    def union_connect(self, x, y):
        x_item = self.find(x)
        y_item = self.find(y)

        if (x_item != y_item):
            self.item[y_item] = x_item
            self.count -= 1


def comp(a, b):
    return a[2] - b[2]


# 处理输入
params = [int(x) for x in input().split(" ")]
n = params[0]
pair_count_1 = params[1]
pair_count_2 = params[2]

# 可建设高铁的两城市
city_pair_1 = []
for i in range(pair_count_1):
    city_pair_1.append([int(x) for x in input().split(" ")])

# 必建高铁的两城市
city_pair_2 = []
for i in range(pair_count_2):
    city_pair_2.append([int(x) for x in input().split(" ")])

uf = UF(n)

# key为修建高铁的两个城市，value为费用
city_map = {}
for city_pair in city_pair_1:
    city1 = city_pair[0]
    city2 = city_pair[1]
    if city1 < city2:
        key = str(city1) + "-" + str(city2)
    else:
        key = str(city2) + "-" + str(city1)
    city_map[key] = city_pair[2]

result = 0
# 先计算必建高铁情况下的费用
for city_pair in city_pair_2:
    city1 = city_pair[0]
    city2 = city_pair[1]
    if city1 < city2:
        key = str(city1) + "-" + str(city2)
    else:
        key = str(city2) + "-" + str(city1)
    result += city_map[key]
    # 纳入并查集
    uf.union_connect(city1, city2)

#  已经满足所有城市通车，直接返回
if (uf.count == 1):
    print(result)
else:
    # 按修建费用排序
    city_pair_1 = sorted(city_pair_1, key=functools.cmp_to_key(comp))

    # 当前的最小权重边
    for city_pair in city_pair_1:
        city1 = city_pair[0]
        city2 = city_pair[1]
        # 判断两城市是否相连
        if (uf.item[city1] != uf.item[city2]):
            uf.union_connect(city1, city2)
            # 若可以合入，则将对应的建造成本计入result
            result += city_pair[2]

        if (uf.count == 1):
            break

    # count>1代表有的城市无法通车
    if (uf.count > 1):
        print(-1)
    else:
        print(result)