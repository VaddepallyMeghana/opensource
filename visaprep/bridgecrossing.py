X, Y, Z = map(int, input().split())
if Z >= Y:
    max_mangoes = (Z - Y)//X
else:
    max_mangoes = 0
    
print(max_mangoes)
