def element(arr,x):
    left,right=0, len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            left=mid+1
        else:
            right=mid-1
    return -1
N=int(input().strip())
arr=list(map(int,input().split()))
x=int(input().strip())
res=element(arr,x)
print(res)
