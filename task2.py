def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return (
                iterations,
                arr[mid],
            )  # Element found; the upper bound is the element itself.
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[
                mid
            ]  # Current element is greater than the target; save as potential upper bound.
            right = mid - 1

    # If the element is not found, return the number of iterations and the upper bound.
    return iterations, upper_bound


# Testing the function:
sorted_array = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8]
target_value = 3.5

result = binary_search_with_upper_bound(sorted_array, target_value)
print(f"Number of iterations: {result[0]}, Upper bound: {result[1]}")
