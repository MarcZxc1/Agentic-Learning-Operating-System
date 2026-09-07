"""Lesson 10: Two pointers on a sorted list."""


def pair_sum_sorted(numbers, target):
    # Problem:
    # numbers is sorted. Return the indices of a pair summing to target,
    # or [-1, -1] when no pair exists.
    #
    # Example: [1, 2, 4, 7, 11], target 9 -> [1, 3]
    #
    # Think:
    # - Put one pointer at each end.
    # - If the sum is too small, which pointer can safely move right?
    # - If the sum is too large, which pointer can safely move left?
    # - Why does sorted order make those moves safe?
    #
    # Hints:
    # - left = 0; right = len(numbers) - 1
    # - Continue while left < right.
    # - Move exactly one pointer after each comparison.
    # - Complexity target: O(n) time and O(1) space.
    pass


print(pair_sum_sorted([1, 2, 4, 7, 11], 9))  # [1, 3]
print(pair_sum_sorted([1, 2, 4, 7, 11], 20)) # [-1, -1]


# Complexity explanation:
# Time: O(n). The left pointer only moves right and the right pointer only
# moves left; together they make at most n pointer moves.
# Space: O(1). We store only the two pointer positions and the current sum.
