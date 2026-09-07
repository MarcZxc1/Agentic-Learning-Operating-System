def calculate_average(score1, score2, score3):
    average = (score1 + score2 + score3) / 3

    return average

average = calculate_average(80, 90, 100)
print(average)


assert calculate_average(80, 90, 100) == 90.0


# Complexity explanation:
# Time: O(1). We always add three scores and divide by 3, regardless of
# how large any other dataset might be.
# Space: O(1). The function uses only a fixed number of variables and does
# not create storage that grows with an input size.


# ---------------------------------------------------------------------------
# CODE BREAKDOWN
# ---------------------------------------------------------------------------
# `def calculate_average(score1, score2, score3):` defines a function. The
# three names are parameters: temporary names for values from the caller.
#
# The next line adds the three inputs and divides the total by 3. The result
# is assigned to `average`.
#
# `return average` sends the value back to the caller; it does not display it.
# The call below receives that value and assigns it to another `average`.
# `print(average)` displays the value.
#
# ERRORS TO RECOGNIZE
# Syntax errors in this current file: none.
# Wrong assignment in this current file: none. Avoid naming a variable `sum`,
# because that shadows Python's built-in sum() function.
# Logic errors to watch for: dividing by the wrong number, forgetting a score,
# or using print() inside the function when a reusable result is needed.
