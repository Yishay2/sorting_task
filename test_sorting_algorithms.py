import random
import matplotlib.pyplot as plt
from heap_sort import build_max_heap
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

arrays = [
    # Small arrays
    [1], [3, 2], [6, 5, 4], [7, 8, 9], [10, 11, 1.5],
    [10, 10, 10, 21], [-3, -1, -4],

    # Medium arrays
    [34, 23, 12, 65, 23, 43, 234, 132],
    [-5, -10, 0, 5, 10, 123],
    [10.5, 2.3, -1.4, 5.0, 3.2, 123.2],
    [100, 100, 100, 100, 100, 100],
    [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 43],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],

    # Large arrays
    [i for i in range(1000)],
    [i for i in range(1000, 0, -1)],
    [random.randint(1, 1000) for _ in range(1000)],
    [random.uniform(-1000, 1000) for _ in range(1000)],
]


def test_algorithms(algorithms, arrays):
    results = {alg_name: {"comparisons": [], "initializations": []} for alg_name in algorithms.keys()}

    for arr in arrays:
        for alg_name, alg_func in algorithms.items():
            arr_copy = arr.copy()
            comparisons, initializations = alg_func(arr_copy)
            results[alg_name]["comparisons"].append(comparisons)
            results[alg_name]["initializations"].append(initializations)

    return results


algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": build_max_heap
}

results = test_algorithms(algorithms, arrays)


def plot_results(results, arrays):
    array_sizes = [len(arr) for arr in arrays]

    for metric in ["comparisons", "initializations"]:
        plt.figure(figsize=(10, 6))
        for alg_name, metrics in results.items():
            plt.plot(array_sizes, metrics[metric], label=alg_name)

        plt.title(f"{metric.capitalize()} vs Array Size")
        plt.xlabel("Array Size")
        plt.ylabel(metric.capitalize())
        plt.legend()
        plt.grid(True)
        plt.show()


plot_results(results, arrays)
