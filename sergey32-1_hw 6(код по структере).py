
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг, показывающий, были ли перестановки на текущей итерации
        swapped = False
        for j in range(0, n - i - 1):
            # Сравниваем элементы и меняем их местами при необходимости
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Если на данной итерации не было перестановок, массив уже отсортирован
        if not swapped:
            break
    return arr
def binary_search(arr, val):
    n = len(arr)
    resultok = False
    first = 0
    last = n - 1

    while first <= last:
        middle = (first + last) // 2
        if arr[middle] == val:
            resultok = True
            position = middle
            break
        elif val > arr[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if resultok:
        print(f"Элемент найден. Позиция: {position}")
    else:
        print("Элемент не найден")

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
val = 7
binary_search(arr, val)