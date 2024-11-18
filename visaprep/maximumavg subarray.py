def max_average_subarray(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum / k
n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(f"{max_average_subarray(nums, k):.4f}")
