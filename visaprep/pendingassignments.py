X, Y, Z = map(int, input().split())
total_time_required = X * Y
total_time_available = Z * 24 * 60
if total_time_required <= total_time_available:
    print("YES")
else:
    print("NO")
