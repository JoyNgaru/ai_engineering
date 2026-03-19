# Radix Sort implementation with Counting Sort as helper

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0–9

    # Count occurrences of each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Convert count to cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (stable sort)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy back to arr
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find maximum number to know number of digits
    max_num = max(arr)
    exp = 1

    # Sort by each digit (LSD → MSD)
    while max_num // exp > 0:
        counting_sort(arr, exp)
        print(f"After sorting by digit at exp={exp}: {arr}")
        exp *= 10


# Test with given phone numbers
phone_numbers = [564, 213, 987, 432, 123, 765, 321, 654, 876]
print("Original list:", phone_numbers)

radix_sort(phone_numbers)

print("Final sorted list:", phone_numbers)
