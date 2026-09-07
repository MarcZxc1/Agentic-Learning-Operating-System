def find_index(numbers, target):
    
    for index, n in enumerate(numbers):
        if n == target:
       
            return index
        
    return -1
        

print(find_index([8, 3, 12, 5], 12))  # 2
print(find_index([8, 3, 12, 5], 9))   # -1
print(find_index([], 9))               # -1


# Complexity explanation:
# Time: O(n) in the worst case because the target may be last or absent.
# Best case is O(1) when the first item matches.
# Space: O(1). The function uses only index and value variables, regardless
# of the list length.


# ---------------------------------------------------------------------------
# CODE BREAKDOWN
# ---------------------------------------------------------------------------
# `enumerate(numbers)` produces (index, value) pairs. For [8, 3, 12], those
# pairs are (0, 8), (1, 3), and (2, 12).
#
# The condition compares the current value with target. When they match,
# returning index stops the search immediately. If the loop finishes, -1 is a
# sentinel meaning the target was not found.
#
# ERRORS TO RECOGNIZE
# Syntax errors in this current file: none.
# Wrong assignment to watch for: confusing `index` and `n`. Returning `n`
# returns the value (12), while this problem asks for its position (2).
# Logic error to watch for: returning -1 inside the loop after the first
# nonmatching item. The search must continue through the remaining values.
