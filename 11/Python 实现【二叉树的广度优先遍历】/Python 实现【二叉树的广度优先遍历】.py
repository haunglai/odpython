class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def TreeFunc(pStr, qStr):
    if len(pStr) == 0:
        return None
    t = TreeNode(pStr[-1])
    i = qStr.index(pStr[-1])

    qRight = qStr[i + 1:]
    qLeft = qStr[:i]
    pLeft = pStr[:len(qLeft)]
    pRight = pStr[len(pLeft):-1]

    t.right = TreeFunc(pRight, qRight)
    t.left = TreeFunc(pLeft, qLeft)
    return t


inputStr = input().strip()
inputList = inputStr.split()
pStr = inputList[0]
qStr = inputList[1]
t = TreeFunc(pStr, qStr)

temStr = ''
temList = []
temList.append(t)
while (len(temList) > 0):
    t = temList[0]
    temList.pop(0)
    if (t is not None):
        temStr += t.value
        temList.append(t.left)
        temList.append(t.right)
print(temStr)