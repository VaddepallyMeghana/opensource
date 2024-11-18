N=int(input())
mat=[]
for _ in range(N):
    row=list(map(int,input().split()))
    mat.append(row)
for row in mat:
    print(" ".join(map(str,row[::-1])))
