T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(max(0, N - M))
