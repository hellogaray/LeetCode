def sliding_window(array, window_size):
    # Edge case: if k is larger than the length of the list
    if len(array) < window_size:
        return None

    # Step 1: Calculate the sum of the first window
    window_sum = sum(array[:window_size])
    max_sum = window_sum

    # Step 2: Slide the window across the rest of the array
    for i in range(len(array) - window_size):
        # Slide the window: subtract the element going out, add the element coming in
        window_sum = window_sum - array[i] + array[i + window_size]

        # Update the max_sum if the new window sum is larger
        max_sum = max(max_sum, window_sum)
    return max_sum
