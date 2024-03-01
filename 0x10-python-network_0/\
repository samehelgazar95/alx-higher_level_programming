#!/usr/bin/python3
"""Find the peak"""


def find_peak(arr):
    """Return the peak with O(n)"""
    if len(arr) == 0 or arr is None:
        return None

    peak = arr[0]
    n = len(arr)

    for i in range(n):
        if i != 0 and i != n-1 and arr[i-1] <= arr[i] >= arr[i+1]:
            if arr[i] > peak:
                peak = arr[i]

    return peak
