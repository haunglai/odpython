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


# 处理输入
n = int(input())

id_pairs = []
for i in range(n):
    id_pairs.append([int(x) for x in input().split(" ")])

id = int(input())

# 发送短信和收到短信的统计信息
send_list = []
receive_list = []

# key为指定ID, value为其send的个数
send_map = {}
# key为指定ID, value为其receive 的个数
receive_map = {}

for id_pair in id_pairs:
    sender = id_pair[0]
    receiver = id_pair[1]

    if (sender == id):
        send_list.append(receiver)
        if receiver in send_map:
            send_map[receiver] += 1
        else:
            send_map[receiver] = 1

    if (receiver == id):
        receive_list.append(sender)
        if sender in receive_map:
            receive_map[sender] += 1
        else:
            receive_map[sender] = 1

# 去重结果
send_set = set(send_list)
receive_set = set(receive_list)

# 交集
intersect = []
for single_id in send_list:
    if single_id in receive_set:
        intersect.append(single_id)

# 两个指标 L & M
L = len(send_set) - len(intersect)
M = len(send_list) - len(receive_list)

flag = False
if (L > 10 or M > 5):
    flag = True

if (not flag):
    # 指标 N
    for single_id in intersect:
        if single_id in send_map \
                and single_id in receive_map \
                and send_map[single_id] - receive_map[single_id] > 5:
            flag = True
            break

print(str(flag) + " " + str(L) + " " + str(M))