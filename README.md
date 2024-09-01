1. Python code for the three sorting algorithms: Insertion Sort, Selection Sort, and Bubble Sort.
2. Selection Sort Correctness Argument
Selection Sort works by repeatedly finding the minimum element from the unsorted portion of the array and swapping it with the first unsorted element. To prove the correctness of Selection Sort, we can use loop invariants.

Invariant: At the start of each iteration of the outer loop (indexed by i), the subarray arr[0:i] is sorted and contains the smallest i elements from the original array in sorted order.

Initialization: Before the first iteration, i = 0, and the subarray arr[0:0] is trivially sorted (an empty subarray).

Maintenance: For each iteration, the algorithm finds the minimum element from the subarray arr[i:n] and places it at arr[i]. This ensures that after placing the minimum element at index i, the subarray arr[0:i+1] remains sorted and contains the smallest i+1 elements.

Termination: The loop terminates when i = n - 1. At this point, the entire array is sorted because all the n elements have been correctly placed in their sorted positions.

Thus, the invariant holds true at every iteration, and upon termination, the array is sorted. This proves the correctness of Selection Sort.

3. To benchmark these algorithms, we'll generate arrays of various sizes, measure the time it takes to sort them, and plot the results. We'll also provide information about the system used for benchmarking.

System Information
CPU: Example: AMD Ryzen 5 5600H with Radeon Graphics @3.30 GHZ
RAM: Example: 20GB DDR4
Operating System: Windows 11
Benchmark Code
Sample Python script to benchmark the runtime of each sorting algorithm:
benchmarking.py
benchmark_Figure.png benchmark of all algorithms
