def bubble_sort(numbers, direction):
    n = len(numbers)
    # Проходим по всем парам элементов списка
    for i in range(n - 1):
        for j in range(n - i - 1):
            # В зависимости от направления сортировки
            if direction == "возрастанию":
                # Если текущий элемент больше следующего, меняем их местами
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            elif direction == "убыванию":
                # Если текущий элемент меньше следующего, меняем их местами
                if numbers[j] < numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Запрашиваем у пользователя количество чисел
n = int(input("Введите количество чисел: "))

# Запрашиваем у пользователя сами числа
numbers = []
for i in range(n):
    number = int(input("Введите число: "))
    numbers.append(number)

# Запрашиваем у пользователя направление сортировки
direction = input("Введите направление сортировки (возрастание/убывание): ")

# Сортируем числа с помощью сортировки пузырьком и заданного направления
bubble_sort(numbers, direction)

# Выводим отсортированный список на экран
print("Отсортированный список:")
for number in numbers:
    print(number)