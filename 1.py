import random

numbers = [random.randint(0, 100) for _ in range(10)]
print(numbers)
number = int(input("Введите число для поиска: "))

def linear(numbers, target):
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1

index = linear(numbers, number)
if index == -1:
    print("Этого числа нет в списке")
else:
    print(f"Число {number} находится на индексе {index}  в списке.")