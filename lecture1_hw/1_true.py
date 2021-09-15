a, b, c = [int(i) for i in input().split()]
if b < c:
    c, b = b, c
if a < b:
    b, a = a, b   
print(a)
