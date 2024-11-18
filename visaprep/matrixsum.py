def matrix_sums(N, matrix):
    row_sums = [0] * N
    col_sums = [0] * N
    for i in range(N):
        for j in range(N):
            row_sums[i] += matrix[i][j]
            col_sums[j] += matrix[i][j]
    result = [row_sums[i] + col_sums[i] for i in range(N)]
    print(" ".join(map(str, result)))
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
matrix_sums(N, matrix)
