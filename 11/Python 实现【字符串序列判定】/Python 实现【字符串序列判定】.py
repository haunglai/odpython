

S = input().strip()
L = input().strip()

res = -1
n = 0
for i in range(len(L)):
    if S[n] == L[i]:
        res = i
        n += 1
    if n == len(S):
        break

print(res)