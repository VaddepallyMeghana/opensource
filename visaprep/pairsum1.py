def has_pair_with_sum(arr, k):
    seen = set()
    for num in arr:
        complement = k - num
        if complement in seen:
            print("true")
            return
        seen.add(num)
    print("false")
N = int(input())  
arr = list(map(int, input().split()))  
K = int(input())
has_pair_with_sum(arr, K)
