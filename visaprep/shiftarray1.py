def rotate_by_one(arr):
    return arr[1:] + arr[:1]
n = int(input())
arr = list(map(int, input().split()))
print(*rotate_by_one(arr))
