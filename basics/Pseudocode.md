2# 1. Average of 3 Numbers
**Input:** score1, score2, score3
**Output:** average of the three scores
**Edge Cases:** Non-numeric inputs (if applicable).
**What must I remember?:** A variable to store the sum before dividing.

**Plain-English Algorithm:**
1. Get the total sum of the 3 inputs.
2. Divide the total by 3 (the number of inputs).
3. Return the calculated average.

# 2. Find the Largest Number
**Input:** A list of numbers (e.g., `[7, 2, 15, 4]`)
**Output:** The largest number in the list.
**Edge Cases:** The list is empty (return None).
**What must I remember?:** A variable `largest` to track the maximum value seen so far.

**Plain-English Algorithm:**
1. Guardrail: If the input list is empty, return None immediately.
2. Assume the first number (index 0) is the largest and store it in `largest`.
3. Loop through every number in the list.
4. If the current number is strictly greater than `largest`, update `largest` to be this current number.
5. After the loop finishes checking all numbers, return `largest`.

# 3. Find Target Index (Linear Search)
**Input:** A list of numbers (e.g., `[8, 3, 12, 5]`) and a `target` (e.g., `12`).
**Output:** The index position of the target.
**Edge Cases:** The target is not in the list (return -1).
**What must I remember?:** Nothing extra, just need to track the current index during the loop.

**Plain-English Algorithm:**
1. Loop through the array, keeping track of the current index and number.
2. If the current number is exactly equal to the target, return the current index immediately.
3. If the loop finishes checking every number and hasn't returned anything, return -1 to indicate the target was not found.

# 4. Count Even Numbers
**Input:** A list of numbers (e.g., `[1, 2, 4, 7, 10]`)
**Output:** The total count of even numbers.
**Edge Cases:** List is empty or contains no even numbers (should return 0).
**What must I remember?:** A `count` accumulator variable.

**Plain-English Algorithm:**
1. Initialize `count` to 0.
2. Loop through every number in the array.
3. If the current number is divisible by 2 with no remainder (`number % 2 == 0`), it is even.
4. If it is even, increment `count` by 1.
5. Once the loop is done, return the final `count`.

# 5. Contains Duplicate
**Input:** A list of numbers (e.g., `[1, 2, 3]` or `[1, 2, 2, 4]` or `[]`)
**Output:** True if any value appears at least twice, False if every element is distinct.
**Edge Cases:** List is empty or has only 1 element (return False).
**What must I remember?:** A `seen` set to store unique elements we have already visited.

**Plain-English Algorithm:**
1. Initialize an empty set called `seen`.
2. Loop through every number in the input list.
3. For each number, check if it is already inside `seen`.
4. If it is already in `seen`, we found a duplicate! Return True immediately.
5. If it is NOT in `seen`, add the current number to the `seen` set.
6. If the loop finishes and hasn't returned True, it means there are no duplicates. Return False.

# 6. Two Sum
**Input:** A list of numbers (e.g., `[2, 7, 11, 15]`) and a `target` (e.g., `9`).
**Output:** The indices of the two numbers that add up to the target.
**Edge Cases:** No valid pair exists (return `[-1, -1]`).
**What must I remember?:** A `seen` dictionary mapping a number to the index where it appeared.

**Plain-English Algorithm:**
1. Initialize an empty dictionary called `seen`.
2. Loop through the numbers, keeping track of both the index and the current number.
3. Calculate the value needed to reach the target: `needed = target - current_number`.
4. Check if `needed` is already a key in our `seen` dictionary.
5. If it IS in the dictionary, we found our pair! Return `[seen[needed], current_index]`.
6. If it is NOT in the dictionary, store the current number in `seen` with its index as the value (`seen[current_number] = current_index`).
7. If the loop finishes and no pair was found, return `[-1, -1]`.
