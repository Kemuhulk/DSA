# METHOD 1:
def quick_sort(arr):
    if len(arr) <= 1:  # Base case: If the list has 0 or 1 element, it's already sorted
        return arr
    
    pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
    left = [x for x in arr if x < pivot]   # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and merge

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

# METHOD 2:
# In-Place Quick Sort (Without Extra Lists)
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1  

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to correct position
    return i + 1  # Return pivot index

def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partition the array
        quick_sort_inplace(arr, low, pi - 1)  # Sort left part
        quick_sort_inplace(arr, pi + 1, high)  # Sort right part

# Example usage:
arr = [64, 25, 12, 22, 11]
quick_sort_inplace(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

# Time Complexity:
# Best case: O(n log n) (Balanced partitions)
# Average case: O(n log n)
# Worst case: O(n²) (When the pivot is always the smallest/largest)
