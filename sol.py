import random
import time
import matplotlib.pyplot as plt

# Генерация случайного списка из 10 элементов
random_list = [random.randint(1, 10000) for _ in range(10000)]
print("Начальный список 10 000 элементов")

# Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Замер времени работы сортировок
def measure_time(sort_function, arr):
    start_time = time.time()
    if sort_function in [quick_sort, merge_sort]:
        sort_function(arr)  # Возвращает новый список
    else:
        sort_function(arr)  # Сортирует на месте
    return time.time() - start_time

# Словарь для хранения времени выполнения каждой сортировки
time_results = {}

# Копирование списка для каждой сортировки
for sort_name, sort_function in {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort
}.items():
    arr_copy = random_list.copy()
    time_results[sort_name] = measure_time(sort_function, arr_copy)

# Вывод времени выполнения каждой сортировки
print("Результаты времени выполнения сортировок:")
for sort_name, timing in time_results.items():
    print(f"{sort_name}: {timing:.10f} секунд")

# Построение гистограммы
plt.bar(time_results.keys(), time_results.values())
plt.ylabel('Время выполнения (секунды)')
plt.title('Сравнение времени выполнения сортировок')
plt.xticks(rotation=45)
plt.show()
