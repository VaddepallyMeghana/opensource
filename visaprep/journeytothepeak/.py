def altitude(h):
    curr_alt=0
    max_alt=0
    for h in H:
        curr_alt+=h
        max_alt=max(max_alt,curr_alt)
    return max_alt
N=int(input().strip())
H=list(map(int,input().split()))
res=altitude(H)
print(res)
