# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

# 处理输入
params = [int(x) for x in input().split(" ")]
rows = params[0]
cols = params[1]

matrix = []
for i in range(rows):
    matrix.append([x for x in input().split(" ")])

# 先将表达式都转为数字
for i in range(rows):
    for j in range(cols):
        if matrix[i][j][0] == '=':
            if '+' in matrix[i][j]:
                op1 = matrix[i][j].split("+")[0]
                op2 = matrix[i][j].split("+")[1]
                # 如果为纯数字，直接取即可
                if op1[1:].isdigit():
                    num1 = int(op1[1:])
                else:
                    # 否则到excel中取到对应位置的数字
                    num1 = int(matrix[int(op1[2:]) - 1][ord(op1[1]) - 65])

                if op2.isdigit():
                    num2 = int(op2)
                else:
                    num2 = int(matrix[int(op2[1:]) - 1][ord(op2[0]) - 65])

                matrix[i][j] = num1 + num2;
            elif '-' in matrix[i][j]:
                op1 = matrix[i][j].split("-")[0]
                op2 = matrix[i][j].split("-")[1]

                if op1[1:].isdigit():
                    num1 = int(op1[1:])
                else:
                    num1 = int(matrix[int(op1[2:]) - 1][ord(op1[1]) - 65])

                if op2.isdigit():
                    num2 = int(op2)
                else:
                    num2 = int(matrix[int(op2[1:]) - 1][ord(op2[0]) - 65])

                matrix[i][j] = num1 - num2
            else:
                matrix[i][j] = int(matrix[int(matrix[i][j][2:]) - 1][ord(matrix[i][j][1]) - 65]);

# 输出表达式解析
output = [x for x in input().split(":")]
res = 0
for i in range(int(output[0][1:]) - 1, int(output[1][1:])):
    for j in range(ord(output[0][0]) - 65, ord(output[1][0]) - 65 + 1):
        res += int(matrix[i][j])

print(res)