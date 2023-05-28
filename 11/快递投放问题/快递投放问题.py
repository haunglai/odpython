# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math
import sys


def comp(a, b):
    return int(a[1]) - int(b[1])


# 处理输入
params = [int(x) for x in input().split(" ")]
m = params[0]
n = params[1]

# 包裹信息
package_info = []
for i in range(m):
    package_info.append(input().split(" "))

# 检查站信息
checkpoint = []
for i in range(n):
    checkpoint.append(input().split(" "))

package_map = {}
checkpoint_map = {}

for single_package in package_info:
    path = single_package[1] + "-" + single_package[2]
    # 合并起点终点作为key
    if path in package_map:
        package_map[path].add(single_package[0])
    else:
        package_map[path] = set()
        package_map[path].add(single_package[0])

for single_checkpoint in checkpoint:
    path = single_checkpoint[0] + "-" + single_checkpoint[1]
    # 合并起点终点作为key
    if path in checkpoint_map:
        for item in single_checkpoint[2:]:
            checkpoint_map[path].add(item)
    else:
        checkpoint_map[path] = set()
        for item in single_checkpoint[2:]:
            checkpoint_map[path].add(item)

result = set()
for key in package_map:
    packages = package_map[key]
    if key not in checkpoint_map:
        continue
    banned_package = checkpoint_map[key]

    for single_package in packages:
        if single_package in banned_package:
            result.add(single_package)

if (len(result) == 0):
    print("none")
else:
    result = list(result)
    sorted(result, key=functools.cmp_to_key(comp))

    print(" ".join(result))

