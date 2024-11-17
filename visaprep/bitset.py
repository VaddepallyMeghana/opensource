def check_kbit(n, x):
    bit = 1 << (x - 1)
    if n & bit:
        return "true"
    else:
        return "false"

n = int(input())  
x = int(input()) 
print(check_kbit(n, x))
