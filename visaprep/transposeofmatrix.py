def transpose_matrix(N, matrix):
    transposed = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            transposed[j][i] = matrix[i][j]
    for row in transposed:
        print(" ".join(map(str, row)))
N = int(input())  
matrix = [list(map(int, input().split())) for _ in range(N)] 
transpose_matrix(N, matrix)
