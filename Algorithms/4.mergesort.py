def merge_sort(arr):
    # Base case: If the array has only one or zero elements, it's already sorted
    if len(arr) > 1:
        # Find the middle index
        mid = len(arr) // 2

        # Split the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0  # i tracks left_half, j tracks right_half, k tracks the main array

        # Merge the two halves into the main array in sorted order
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from left_half (if any)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half (if any)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)

merge_sort(arr)  # Sort the array using Merge Sort

print("Sorted array:", arr)


# EXPLANATION OF KEY STEPS

# 1.Splitting the Array:
# -The array is divided into two halves recursively until each sub-array has only one element.

# 2.Sorting and Merging:
# -Two sorted halves are merged by comparing elements and placing them in sorted order.
# -Remaining elements (if any) from each half are added at the end.

# COMPLEXITY ANALYSIS

# -Best Case: O(n log n)
# -Average Case: O(n log n)
# -Worst Case: O(n log n)
# -Space Complexity: O(n) (extra space for merging)
