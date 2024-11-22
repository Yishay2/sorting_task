import random


def merge(a, start, mid, end):
    comparisons = initialization = 0
    i = j = 0
    left = a[start: mid + 1]
    right = a[mid + 1: end + 1]
    k = start
    comparisons += 1
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        initialization += 1
        k += 1

    while i < len(left):
        a[k] = left[i]
        initialization += 1
        i += 1
        k += 1


    return comparisons, initialization


def __merge_sort(a, start, end):
    comparisons = initialization = 0
    if start < end:
        mid = (start + end) // 2
        c1, i1 = __merge_sort(a, start, mid)
        c2, i2 = __merge_sort(a, mid + 1, end)
        c3, i3 = merge(a, start, mid, end)
        comparisons += c1 + c2 + c3
        initialization += i1 + i2 + i3
    return comparisons, initialization


def merge_sort(a):
    return __merge_sort(a, 0, len(a) - 1)
