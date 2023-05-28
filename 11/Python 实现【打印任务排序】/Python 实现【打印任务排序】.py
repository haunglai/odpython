from collections import deque

nums = list(map(int, input().split(",")))
nums_list = list(enumerate(nums))

# 队列的使用
queue = deque()
for num in nums_list:
    queue.append((num[0], num[1]))

ans, count = list(), 0
while True:
    if len(queue) <= 1:
        break
    task = queue.popleft()
    cur_max = max(queue, key=lambda x: x[1])
    if task[1] >= cur_max[1]:
        ans.append((task[0], count))
        count += 1
    else:
        queue.append(task)
ans.append((queue[0][0], count))

print(",".join(map(lambda x: str(x[1]), sorted(ans, key=lambda x: x[0]))))