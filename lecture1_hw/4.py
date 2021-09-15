a = [int(i) for i in input().split()]
cnt = 0
for i in a:
    cnt += (i == 0)
print(cnt)
