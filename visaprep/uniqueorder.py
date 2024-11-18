def get_unique_elements(arr):
    seen = set()  
    unique = []   
    
    for num in arr:
        if num not in seen: 
            unique.append(num) 
            seen.add(num)      
    return unique
n = int(input())
arr = list(map(int, input().split()))
print(*get_unique_elements(arr))
