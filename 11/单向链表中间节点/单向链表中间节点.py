# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import copy


# 链表节点类
class ListNode:
    def __init__(self, val="", next=None):
        self.val = val
        self.next = next


# 处理输入
head = input().split(" ")
head_addr = head[0]
list_count = int(head[1])

# 构造节点信息map
node_info = {}
for i in range(list_count):
    # 节点信息
    input_node_info = input().split(" ")
    addr = input_node_info[0]
    val = int(input_node_info[1])
    next_addr = input_node_info[2]
    temp_node = ListNode(val, next_addr)
    node_info[addr] = temp_node

# 构造链表，剔除无效节点
size = 1
cur = 0
head_node = node_info[head_addr]
thead = copy.copy(head_node)
while (thead.next != '-1'):
    size += 1
    thead = node_info[thead.next]

# 找中间节点
while (head_node.next != -1):
    if (int(size / 2) == cur):
        print(head_node.val)
        break;
    head_node = node_info[head_node.next]
    cur += 1



