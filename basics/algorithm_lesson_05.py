def contains_duplicate(numbers):
    seen = set()

    for nums in numbers:
        if nums in seen:
            return True
        else:
            seen.add(nums)
    return  False


print(contains_duplicate([1, 2, 3]))      # False
print(contains_duplicate([1, 2, 2, 4]))   # True
print(contains_duplicate([]))             # False


# Complexity explanation:
# Time: O(n) average. Set membership and insertion are O(1) on average, and
# we may process every number once. The function can stop early on a repeat.
# Space: O(n). In the no-duplicate case, `seen` stores every input value.


# ---------------------------------------------------------------------------
# CODE BREAKDOWN
# ---------------------------------------------------------------------------
# `seen = set()` creates memory of values already visited. For each number,
# membership is checked first. If it is already present, the function returns
# True immediately. Otherwise it is added for future checks.
#
# If the loop finishes, every value was unique, so False is returned.
#
# ERRORS TO RECOGNIZE
# Syntax errors in this current file: none.
# Wrong assignment to watch for: using `seen = number`, which replaces the
# set, instead of `seen.add(number)`, which adds to it.
# Logic error to watch for: adding before checking. The current value would
# always be found immediately and every nonempty list would look duplicated.
# `set.add()` changes the set and returns None; it is not the new set value.

