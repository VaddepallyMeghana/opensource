T = int(input().strip())
results = []
for _ in range(T):
    X, N = map(int, input().split())
    score = (X // 10) * N
    results.append(score)
for result in results:
    print(result)
