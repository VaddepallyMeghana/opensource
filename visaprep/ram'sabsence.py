def max_consecutive_absent_days(n, attendance):
    max_absent_streak = 0 
    current_streak = 0  
    
    for i in range(n):
        if attendance[i] == 0:
            current_streak += 1  
        else:
            max_absent_streak = max(max_absent_streak, current_streak)  
            current_streak = 0  
    max_absent_streak = max(max_absent_streak, current_streak)
    
    return max_absent_streak
n = int(input())
attendance = list(map(int, input().split()))
print(max_consecutive_absent_days(n, attendance))
