x1, y1 = list(map(int, input().split(" ")))
x2, y2 = list(map(int, input().split(" ")))
d = abs(x1-x2) + abs(y1-y2)
print(d)