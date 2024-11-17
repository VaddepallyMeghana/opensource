def print_triangle(N):
    for i in range(1, N+1):
        print(" ".join([str(i)] * i))
N = int(input())
print_triangle(N)
