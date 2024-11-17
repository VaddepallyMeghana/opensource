o = int(input())
for _ in range(o):
    a, b = map(int, input().split())
    score = a//10
    sc = score*b
    print(sc)
