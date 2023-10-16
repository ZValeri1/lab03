def bubble_sort(numbers):
    n = len(numbers)
    # Проходим по всем парам элементов списка
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Запрашиваем у пользователя количество чисел
n = int(input("Введите количество чисел: "))

# Запрашиваем у пользователя сами числа
numbers = []
for i in range(n):
    number = int(input("Введите число: "))
    numbers.append(number)

# Сортируем числа с помощью сортировки пузырьком
bubble_sort(numbers)

# Выводим отсортированный список на экран
print("Отсортированный список:")
for number in numbers:
    print(number)