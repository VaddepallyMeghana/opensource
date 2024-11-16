A, B, C, X = map(int, input().split())
if A + B >= X or B + C >= X or A + C >= X:
    print("YES")
else:
    print("NO")
