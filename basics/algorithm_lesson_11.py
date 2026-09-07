"""Lesson 11: Fixed-size sliding window."""


def max_sum_window(numbers, k):
    # Problem:
    # Return the largest sum of any contiguous window of exactly k values.
    # Return None when k <= 0, numbers is empty, or k > len(numbers).
    #
    # Example: [2, 1, 5, 1, 3, 2], k=3 -> 9 (5 + 1 + 3)
    #
    # Brute force would sum each window from scratch. That repeats work.
    # Sliding-window idea:
    # - Build the first window once.
    # - When moving right, add the new right value.
    # - Remove the value that just left on the left.
    # - Track the best window sum.
    #
    # Hints:
    # - `window_sum = sum(numbers[:k])` is allowed here.
    # - For right in range(k, len(numbers)):
    # - Remove numbers[right - k].
    # - Complexity target: O(n) time and O(1) extra space.
    pass


print(max_sum_window([2, 1, 5, 1, 3, 2], 3))  # 9
print(max_sum_window([1, 2], 3))              # None


# Complexity explanation:
# Time: O(n). The first window is built once, then every move adds one value
# and removes one value instead of summing each window from scratch.
# Space: O(1) extra space. We keep only the current sum, best sum, and indexes;
# the input list itself is not counted as extra space.
