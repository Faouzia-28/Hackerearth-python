def count_divisibles(l, r, k):
    # Find the first number in the range [l, r] that is divisible by k
    if l % k == 0:
        first_divisible = l
    else:
        first_divisible = l + (k - l % k)
    
    # Find the last number in the range [l, r] that is divisible by k
    if r % k == 0:
        last_divisible = r
    else:
        last_divisible = r - (r % k)
    
    # Calculate the count of divisible numbers
    if first_divisible > r or last_divisible < l:
        count = 0
    else:
        count = (last_divisible - first_divisible) // k + 1
    
    return count

# Read input
l, r, k = map(int, input().split())

# Calculate and print the result
print(count_divisibles(l, r, k))