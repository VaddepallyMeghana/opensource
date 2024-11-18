def rotate_array(N, arr, K):
    K = K % N
    rotated_arr = arr[-K:] + arr[:-K]
    print(" ".join(map(str, rotated_arr)))
N = int(input())  
arr = list(map(int, input().split()))  
K = int(input()) 
rotate_array(N, arr, K)
