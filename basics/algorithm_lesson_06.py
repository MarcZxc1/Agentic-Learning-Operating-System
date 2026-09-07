"""Lesson 6: Two Sum with a dictionary.

Pattern: remember previous values so we do not repeatedly search the list.
"""


def two_sum(numbers, target):
    # Problem:
    # Return the indices of two different numbers whose sum equals target.
    # Return [-1, -1] if no pair exists.
    #
    # Before coding, trace [2, 7, 11, 15] with target 9.
    # At each position ask: what number would complete the target?
    #
    # Hints:
    # - needed = target - number
    # - `seen` should map a number to the index where it appeared.
    # - Check whether `needed` is already in seen BEFORE storing number.
    # - Return [seen[needed], index] when found.
    # - Edge cases: empty list, no pair, negative numbers, duplicate values.
    # - Target complexity: O(n) average time and O(n) extra space.

    seen = {}
    
    for index, num in enumerate(numbers):
        needed = target - num

        if needed in seen:
            prev_index = seen[needed]
            return [prev_index, index]
        seen[num] = index

    return [-1, -1]    


    
           
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]
print(two_sum([1, 2, 3], 10))      # [-1, -1]


# Complexity explanation:
# Time: O(n) average. We make one pass, and dictionary lookup/insertion is
# O(1) on average. A brute-force pair comparison would be O(n^2).
# Space: O(n). The `seen` dictionary may store almost every number and index.
