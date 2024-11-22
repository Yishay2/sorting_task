import random
arr = [random.randint(1, 100) for _ in range(10)]

def left_child_index(i):
    return 2 * i + 1

def right_child_index(i):
    return 2 * i + 2

def parent_index(i):
    return (i - 1) // 2

def max_heapify(arr, i, heap_size):
    comparisons = initialization = 0
    l = left_child_index(i)
    r = right_child_index(i)
    largest = i
    initialization += 3
    if l < heap_size and arr[l] > arr[i]:
        largest = l
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        comparisons += 2
        arr[i], arr[largest] = arr[largest], arr[i]
        c, i =max_heapify(arr, largest, heap_size)
        comparisons += c
        initialization += i
    return comparisons, initialization


def __build_max_heap(arr):
    comparisons = initialization = 0
    heap_size = len(arr)
    for i in range((heap_size - 1), -1, -1):
        c, i = max_heapify(arr, i, heap_size)
        comparisons += c
        initialization += i
    return comparisons, initialization


def build_max_heap(arr):
    return __build_max_heap(arr)
