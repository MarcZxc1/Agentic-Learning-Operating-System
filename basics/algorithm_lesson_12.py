"""Lesson 12: Variable-size sliding window."""


def longest_without_repeating(text):
    # Problem:
    # Return the length of the longest substring with no repeated characters.
    # A substring must be contiguous. Examples: "abcabcbb" -> 3, "bbbbb" -> 1.
    #
    # Window invariant:
    # text[left:right + 1] contains no repeated characters.
    #
    # Think:
    # - Expand right one character at a time.
    # - What does a repeated character tell you about left?
    # - How can a dictionary store the most recent index of each character?
    # - Never move left backwards.
    #
    # Hints:
    # - Use `last_seen = {}`.
    # - If a character was seen inside the current window, move left to one
    #   position after its previous index.
    # - Update last_seen for every character.
    # - Track the best length with right - left + 1.
    # - Complexity target: O(n) time and O(k) space.
    pass


print(longest_without_repeating("abcabcbb"))  # 3
print(longest_without_repeating("bbbbb"))    # 1
print(longest_without_repeating(""))         # 0


# Complexity explanation:
# Time: O(n) average. The right pointer moves forward once, and left never
# moves backward; dictionary lookups are O(1) on average.
# Space: O(k), where k is the number of distinct characters in the current
# input, because `last_seen` stores one position per character.
