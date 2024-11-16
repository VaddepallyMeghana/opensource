X=int(input())
if (X%400==0) or (X%4==0 and X%100!=0):
    print("YES")
else:
    print("NO")
