# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools


def comp(a, b):
    return int(a[1]) - int(b[1])


# 处理输入
n = int(input())
clock_records = []
for i in range(n):
    clock_records.append(input().split(","))

# 存放每位员工的打卡记录
record_map = {}
result = set()

# 初始化map时实现异常规则1
for i in range(n):
    # 题目要求按输入顺序输出，加一个索引 i
    single_record = clock_records[i]
    clock_records[i].append(str(i));

    if (single_record[3] != (single_record[4])):
        result.add(i);
    else:
        if (single_record[0] in record_map):
            record_map[single_record[0]].append(single_record)
        else:
            record_map[single_record[0]] = []
            record_map[single_record[0]].append(single_record)

# 异常规则2
for key in record_map:
    records = record_map[key];

    # 用打卡时间来排序，以加速后续的双层循环。
    records = sorted(records, key=functools.cmp_to_key(comp))
    # records.sort((a, b) -> Integer.parseInt(a[1]) - Integer.parseInt(b[1]));

    for i in range(len(records)):
        time1 = int(records[i][1])
        dist1 = int(records[i][2])
        for j in range(i + 1, len(records)):
            time2 = int(records[j][1])
            dist2 = int(records[j][2])

            # 如果当前的两次打卡时间超过60分, 那么后面的肯定也超过60分钟了
            if (time2 - time1 >= 60):
                break
            else:
                if (abs(dist2 - dist1) > 5):
                    result.add(int(records[i][5]))
                    result.add(int(records[j][5]))

# 输出
if (len(result) == 0):
    print("null")
else:
    res_str = "";
    for index in result:
        clock_records[index].pop()
        res_str += ",".join(clock_records[index]) + ";"
    print(res_str[0:len(res_str) - 1]);



