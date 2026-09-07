"""Lesson 8: Stack pattern — matching brackets."""


def is_balanced(text):
    # Problem:
    # Return True when every opening bracket has the correct closing bracket.
    # Supported brackets: (), [], {}
    # Examples: "([])" -> True, "([)]" -> False.
    #
    # Think before coding:
    # - Which opening bracket must be closed first? (The most recent one.)
    # - Which data structure gives last-in, first-out behavior?
    # - What should happen when a closing bracket appears with no opener?
    #
    # Hints:
    # - Use a list as a stack and `.append()` / `.pop()`.
    # - Map closing brackets to their expected opening brackets.
    # - On an opener, push it.
    # - On a closer, check that the stack is non-empty and its top matches.
    # - At the end, the stack must be empty.
    # - Complexity target: O(n) time and O(n) space.
    pass


print(is_balanced("([])"))  # True
print(is_balanced("([)]"))  # False
print(is_balanced(""))      # True


# Complexity explanation:
# Time: O(n). Each bracket is pushed or popped at most once.
# Space: O(n) in the worst case, when the input contains n opening brackets
# before any closing brackets; the stack must store all of them.
