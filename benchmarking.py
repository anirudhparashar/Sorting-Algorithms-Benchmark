import random
import time
import matplotlib.pyplot as plt
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break
    return arr

def benchmark_sorting_algorithm(sort_func, sizes):
    times = []
    for size in sizes:
        # Generate a random array of the given size
        arr = [random.randint(1, 10000) for _ in range(size)]
        # Time the sorting function
        start_time = time.time()
        sort_func(arr)
        end_time = time.time()
        # Record the elapsed time
        times.append(end_time - start_time)
    return times

# Define input sizes for benchmarking
sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

# Benchmark each sorting algorithm
insertion_sort_times = benchmark_sorting_algorithm(insertion_sort, sizes)
selection_sort_times = benchmark_sorting_algorithm(selection_sort, sizes)
bubble_sort_times = benchmark_sorting_algorithm(bubble_sort, sizes)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_sort_times, label='Insertion Sort', marker='o')
plt.plot(sizes, selection_sort_times, label='Selection Sort', marker='o')
plt.plot(sizes, bubble_sort_times, label='Bubble Sort', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Benchmark of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()
