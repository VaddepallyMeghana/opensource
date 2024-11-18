def reverse_integer(n):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1  
    negative = n < 0                      
    reversed_num = int(str(abs(n))[::-1]) 
    if negative:
        reversed_num = -reversed_num      
    if reversed_num < INT_MIN or reversed_num > INT_MAX:  
        return 0                         
    return reversed_num                  

n = int(input())  
print(reverse_integer(n))
