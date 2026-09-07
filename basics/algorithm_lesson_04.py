def count_even(numbers):
    if not numbers:
        return 0


    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
        

    return count        

print(count_even([1, 2, 4, 7, 10]))  # 3
print(count_even([1, 3, 5]))         # 0
print(count_even([]))


# Complexity explanation:
# Time: O(n). We inspect each number once to decide whether it is even.
# Space: O(1). The accumulator `count` is one variable and does not grow
# with the number of input values.


# ---------------------------------------------------------------------------
# CODE BREAKDOWN
# ---------------------------------------------------------------------------
# `count = 0` is an accumulator: it stores the answer built so far.
# Each iteration tests one number. `%` gives a remainder; remainder 0 after
# division by 2 means the number is even.
#
# `count += 1` means `count = count + 1`. It updates the answer only when the
# condition is true. An empty list correctly produces 0; the explicit check is
# optional because the loop would run zero times.
#
# ERRORS TO RECOGNIZE
# Syntax errors in this current file: none.
# Wrong assignment to watch for: changing `number` instead of incrementing
# `count`, or resetting `count = 0` inside the loop.
# Logic errors to watch for: testing remainder 1 when the task asks for evens,
# or placing the return before the loop finishes.
