def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftHalf = arr[:mid]
        right_half = arr[mid:]

        mergeSort(leftHalf)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(leftHalf) and j < len(right_half):
            if leftHalf[i] >= right_half[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def main():
    # Введення 5 чисел
    numbers = []
    for i in range(5):
        num = int(input(f"Введіть число {i + 1}: "))
        numbers.append(num)

    # Виклик рекурсивної функції сортування
    mergeSort(numbers)

    # Виведення відсортованого масиву
    print("Відсортований масив за не зростанням:", numbers)



