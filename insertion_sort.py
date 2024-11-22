def insertion_sort(arr):
    n = len(arr)
    count_of_comparisions = count_of_initializations = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        count_of_comparisions += 1
        while j >= 0 and arr[j] > key:
            count_of_comparisions += 1
            count_of_initializations += 1
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        count_of_initializations += 1

    return count_of_initializations, count_of_comparisions
