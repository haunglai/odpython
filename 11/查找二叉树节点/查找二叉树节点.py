# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
        size = len(queue)
        tmp = []
        # 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
        # 如果节点的左/右子树不为空，也放入队列中
        for i in range(size):
            r = queue.pop(0)
            tmp.append(r.val)
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
        # 将临时list加入最终返回结果中
        res.append(tmp)
    return res


# 处理输入
n = int(input())

nodes_info = []
for i in range(n):
    nodes_info.append([int(x) for x in input().split(" ")])

target_info = [int(x) for x in input().split(" ")]
x = target_info[0]
y = target_info[1]

# 初始化二叉树
nodes = []
for i in range(n):
    nodes.append(TreeNode(nodes_info[i][0]))

for i in range(n):
    if (len(nodes_info[i]) > 1):
        nodes[i].left = nodes[nodes_info[i][1]]
    if (len(nodes_info[i]) > 2):
        nodes[i].right = nodes[nodes_info[i][2]]

result = levelOrder(nodes[0])
res_str = "{" + str(result[x][y]) + "}"
print(res_str)