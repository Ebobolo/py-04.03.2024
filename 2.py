import random

numbers = sorted([random.randint(0, 100) for _ in range(10)])
print(numbers)
number_to_find = int(input("Введите число для поиска: "))

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

index = binary_search(numbers, number_to_find)

# Print the result
if index == -1:
    print("Этого числа нет в списке")
else:
    print(f"число {number_to_find} находится на индексе {index} в списке.")
