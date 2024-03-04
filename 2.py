import random

# Create a sorted list of 10 random numbers
numbers = sorted([random.randint(0, 100) for _ in range(10)])

# Get the number to search for from the user
number_to_find = int(input("Enter a number to search for: "))

# Implement the binary search algorithm
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    # Continue searching until the left pointer is greater than the right pointer
    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Call the binary search function with the sorted list and the number to find
index = binary_search(numbers, number_to_find)

# Print the result
if index == -1:
    print("That number is not in the list.")
else:
    print(f"The number {number_to_find} is at index {index} in the list.")