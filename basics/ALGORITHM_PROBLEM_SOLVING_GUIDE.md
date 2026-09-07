# How to Understand and Solve Algorithm Problems

Use this process every time you solve a problem. Do not begin by trying to
remember code. Begin by understanding the problem.

## 1. Translate the problem

Identify three things:

```text
Input: What data am I given?
Output: What must I return?
Rules: What conditions must be followed?
```

Example: “Find the largest number in a list.”

```text
Input: a list of numbers
Output: one number
Rule: return the greatest value
```

## 2. Work through a small example manually

For:

```python
[7, 2, 15, 4]
```

Think:

```text
current largest = 7
compare 2  -> keep 7
compare 15 -> update to 15
compare 4  -> keep 15
answer = 15
```

Manual tracing helps you discover the algorithm before you write Python.

## 3. Write plain-English steps

Before coding, write something like:

```text
1. If the list is empty, return None.
2. Treat the first number as the largest so far.
3. Visit every number.
4. If a number is larger, update largest.
5. Return largest.
```

If you cannot explain the steps without code, you probably do not understand
the problem yet.

## 4. Identify what the algorithm must remember

Ask:

> What information must I carry from one loop iteration to the next?

Common examples:

| Problem need | State to remember | Python structure |
|---|---|---|
| Largest value | `largest` | variable |
| Number of matches | `count` | accumulator variable |
| Already-seen values | `seen` | set |
| Value-to-index relationship | `seen` | dictionary |
| Current search range | `left`, `right` | variables |
| Recently opened brackets | `stack` | list used as a stack |

## 5. Start with the simplest correct solution

Do not optimize before the logic works. First create a correct baseline:

```python
def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest
```

Correctness comes before cleverness.

## 6. Trace your code

Make a small table showing how important variables change:

| Number | Current largest |
|---:|---:|
| 7 | 7 |
| 2 | 7 |
| 15 | 15 |
| 4 | 15 |

This changing fact is called an **invariant**: after every iteration,
`largest` is the greatest value seen so far.

## 7. Test edge cases

Always consider:

```python
[]                 # empty input
[one_item]         # smallest nonempty input
[target_missing]   # requested value does not exist
[duplicate_values] # repeated data
[negative_values]  # values below zero
```

Also test the ordinary example from the problem statement.

## 8. Analyze complexity

Ask two questions:

1. How many times can the algorithm do work as the input grows?
2. What additional memory grows with the input?

Basic patterns:

```text
Fixed number of operations       -> O(1) time
One loop through n items         -> O(n) time
Nested loops through n items     -> O(n²) time
Halving the search range         -> O(log n) time
Only a few variables             -> O(1) extra space
Extra collection holding n items -> O(n) extra space
```

## 9. Improve only when there is a reason

Compare a brute-force idea with a better pattern:

| Situation | Useful pattern |
|---|---|
| Need to inspect every item | Linear scan |
| Need quick “have I seen this?” checks | Set |
| Need value-to-index lookup | Dictionary |
| Sorted input and a target search | Binary search |
| Pair in a sorted list | Two pointers |
| Contiguous range with a constraint | Sliding window |
| Most recent unfinished item | Stack |

Ask why the optimization is valid. Do not use a pattern just because it is
popular.

## A reusable solving template

Copy this into your notes for each new problem:

```text
Problem:

Input:
Output:
Rules/constraints:

Small example:

Plain-English algorithm:
1.
2.
3.

What must I remember?

Edge cases:

Brute-force complexity:
Better approach (if needed):
Time complexity:
Space complexity:
```

The central habit is:

> Understand the input, manually solve one example, identify what must be
> remembered, and write the steps in English before writing code.
