def find_largest(numbers):
    if not numbers:
        return  None
    
    largest = numbers[0]
    
    for n in numbers:
        if n > largest:
            largest = n
    
      

    return largest

print(find_largest([7, 2, 15, 4])) 
print(find_largest([3, 9, 1]))  

print(find_largest([]))


# Complexity explanation:
# Time: O(n). In the worst case, the loop checks every number in the list.
# Space: O(1). We keep only the current largest value; no new list grows
# with the input.


# ---------------------------------------------------------------------------
# CODE BREAKDOWN
# ---------------------------------------------------------------------------
# `if not numbers:` handles the empty-list edge case before numbers[0] is used.
# Returning None means there is no largest value for an empty input.
#
# `largest = numbers[0]` initializes the current best answer with the first
# value. It does not claim that the first value is globally largest yet.
# The loop compares every value and replaces `largest` when a bigger value is
# found. After the loop, it is the biggest value seen.
#
# ERRORS TO RECOGNIZE
# Syntax errors in this current file: none.
# Wrong assignment to watch for: writing `n = largest` instead of
# `largest = n`. Update the answer, not the value being inspected.
# Logic errors to watch for: omitting the empty-list check, or returning
# inside the loop after the first nonmatch instead of after the full search.
