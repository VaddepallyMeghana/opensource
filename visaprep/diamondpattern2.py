def print_diamond_pattern(n):
    # Top part of the diamond
    for i in range(1, n + 1):
        stars = "*" * i
        spaces = " " * (2 * (n - i))
        print(stars + spaces + stars)
    
    # Bottom part of the diamond
    for i in range(n - 1, 0, -1):
        stars = "*" * i
        spaces = " " * (2 * (n - i))
        print(stars + spaces + stars)

# Input
n = int(input().strip())

# Print the pattern
print_diamond_pattern(n)
