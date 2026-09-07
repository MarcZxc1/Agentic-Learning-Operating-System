"""Lesson 9: Binary search on a sorted list."""


def binary_search(numbers, target):
    # Problem:
    # numbers is sorted in ascending order. Return target's index, or -1.
    #
    # Trace this by hand first:
    # numbers = [1, 3, 5, 7, 9, 11], target = 9
    #
    # Invariant (what stays true):
    # If target exists, it is inside the current left..right search range.
    #
    # Hints:
    # - Start left = 0 and right = len(numbers) - 1.
    # - Continue while left <= right.
    # - middle = (left + right) // 2.
    # - If numbers[middle] == target, return middle.
    # - If the middle value is too small, move left to middle + 1.
    # - Otherwise move right to middle - 1.
    # - Complexity target: O(log n) time and O(1) space.
    pass


print(binary_search([1, 3, 5, 7, 9, 11], 9))  # 4
print(binary_search([1, 3, 5, 7, 9, 11], 4))  # -1
print(binary_search([], 4))                   # -1


# Complexity explanation:
# Time: O(log n). Each comparison removes about half of the remaining search
# range, so the work grows logarithmically rather than checking every item.
# Space: O(1). The iterative version stores only left, right, and middle.
