"""Lesson 7: Frequency counting with a dictionary."""


def first_unique_character(text: str) -> int:
    # Problem:
    # Return the index of the first character that appears exactly once.
    # Return -1 when every character is repeated or text is empty.
    # Decide whether uppercase and lowercase should be different; for this
    # exercise, treat them as different characters.
    #
    # Example: "swiss" -> 1 because 'w' is the first unique character.
    #
    # Problem-solving steps:
    # 1. What must be counted before we can decide uniqueness?
    # 2. Why might one pass count and a second pass find the answer?
    # 3. Trace the dictionary after each character in "swiss".
    #
    # Hints:
    # - First pass: counts[character] = counts.get(character, 0) + 1
    # - Second pass: return the first index whose count is 1.
    # - Complexity target: O(n) time and O(k) space, where k is unique chars.
    if not text:
        return -1 

    count = {}

    for char in text:
        count[char] = count.get(char, 0) + 1

       

    for i, n in enumerate(text):
        if count[n] == 1:
            return i
        


    return -1


print(first_unique_character("swiss"))  # 1
print(first_unique_character("aabb"))   # -1
print(first_unique_character(""))       # -1

"""
    =========================================
    FULL DSA WRITTEN SCAFFOLD (Fill this out)
    =========================================
    
    1. APPROACH / MENTAL MODEL:
    (Explain how you are going to solve this in plain English using a dictionary)
    > To solve this is I need to add a condition for checking the text if its empty or the character is repetitve and should gives -1.
    Second, initialize a dictionary for storing the characters
    Third is scan the text and if the character is not in count dictionary start with 0 then add 1 and if the character is in the count add 1.
    Fourth is scan the dictionary or list and if the character is seen once, return 1
    Fifth is the fallback, if its repetitve return -1
    
    
    2. EDGE CASES HANDLED:
    (What are the sneaky inputs you need to watch out for? e.g., empty string, all duplicates)
    > If the text is empty return -1 immediately, because there is nothing to check
    Normal String: For a string like "swiss" it scans the entire text and counts is frequency and and since the second character is w and it is only one,
    return 1 because it is the first unique character seen in the text
    All duplicates: if the text is repetitve like aabb return immediately -1 because there is no unique character
    
    3. INTERVIEW TRACE:
    (Trace the dictionary state character by character for the input "swiss", then trace the second pass)
    > PASS 1
    s | count = {s = 1} | count = {s = 1}
    w | count = {s = 1} | count = {s = 1, w = 1}
    i | count = {s = 1 w = 1} | count = {s = 1, w = 1, i = 1}
    s | count = {s = 1, w = 1, i = 1} | count = {s = 2, w = 1, i = 1}
    s | count = {s = 2, w = 1, i = 1} | count = {s = 3, w = 1, i = 1}
    
    PASS 2: 
    Index 0: s: count = 3 SKIP
    Index 1: w: count = 1 Return because is the first unique character


    4. COMPLEXITY JUSTIFICATION:
    - Time Complexity: O(n) - Why? Becuse it uses for loop to look at every element and that is n. 
    > 
    - Space Complexity: O(k) - Why? The dictionary stores unique characters. If the string has k unique characters, 
    the dictionary takes up $k$ space. (Note: If the input is restricted strictly to the lowercase English alphabet, 
    the space complexity is technically $O(1)$ because the dictionary can never grow larger than 26 items, no matter how long the text is
    > 
    """
