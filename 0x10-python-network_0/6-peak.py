#!/usr/bin/python3
""" find peak in a table """


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - The peak element in the list.
    """
    # Get the length of the list
    n = len(list_of_integers)

    # Check if the list is empty
    if n == 0:
        return None

    # Initialize start and end indices for binary search
    start = 0
    end = n - 1

    # Perform binary search to find the peak
    while start < end:
        mid = (start + end) // 2
        # Check if the mid element is greater than its neighbors
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Check if it's also greater than its left neighbor
            if mid == 0 or list_of_integers[mid] > list_of_integers[mid - 1]:
                return list_of_integers[mid]
            else:
                end = mid - 1
        else:
            start = mid + 1

    # If peak is at the last element, return it
    return list_of_integers[start]
