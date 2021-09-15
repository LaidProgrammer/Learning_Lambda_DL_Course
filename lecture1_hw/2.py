a, b, c = [int(i) for i in input().split()]
if a == b and b == c:
    print(3)
elif a == b:
    print(2)
elif b == c:
    print(2)
elif a == c:
    print(2)
else:
    print(0)
