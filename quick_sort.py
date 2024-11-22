import random


def randomise_partition(a, start, end):
    comparisons = initialization = 0
    random_index = random.randint(start, end)
    initialization += 2
    a[random_index], a[end] = a[end], a[random_index]
    i = start - 1
    for j in range(start, end):
        comparisons += 1
        if a[j] <= a[end]:
            initialization += 2
            i += 1
            a[j], a[i] = a[i], a[j]
    a[i + 1], a[end] = a[end], a[i + 1]
    initialization += 2
    return i + 1, comparisons, initialization


def __quick_sort(a, start, end):
    comparisons = initialization = 0
    if start < end:
        q, c, i = randomise_partition(a, start, end)
        left_comparisons, left_initialization = __quick_sort(a, start, q - 1)
        right_comparisons, right_initialization = __quick_sort(a, q + 1, end)
        comparisons = c + left_comparisons + right_comparisons
        initialization = i + left_initialization + right_initialization
    return comparisons, initialization


def quick_sort(a):
    return __quick_sort(a, 0, len(a) - 1)
