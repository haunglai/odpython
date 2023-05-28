
n = int(input())

a = input()
b = input()
c = []
cnt = [0] * 2
for i in range(n):
    if b[i] == '0':
        c.append(int(a[i]))
    if a[i] == '0':
        cnt[0] += 1
    else:
        cnt[1] += 1
total = 0

for i in range(len(c)):
    total += cnt[c[i] ^ 1]
    cnt[c[i]] -= 1

print(total)