from collections import Counter

def frequency_sort(nums):
    # Count the frequency of each element
    freq = Counter(nums)
    
    # Sort by frequency (ascending), and by value (descending) for ties
    nums.sort(key=lambda x: (freq[x], -x))
    return nums

# Input reading
n = int(input().strip())  # Size of the array
nums = list(map(int, input().strip().split()))  # Array elements

# Sorting and printing the result
result = frequency_sort(nums)
print(" ".join(map(str, result)))
