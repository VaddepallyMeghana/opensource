def fix_grid(N, M, grid):
    rows_to_zero = set() 
    cols_to_zero = set()   
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)
    for i in range(N):
        for j in range(M):
            if i in rows_to_zero or j in cols_to_zero:
                grid[i][j] = 0
    for row in grid:
        print(' '.join(map(str, row)))

N, M = map(int, input().split()) 
grid = [list(map(int, input().split())) for _ in range(N)] 
fix_grid(N, M, grid)
