# 2011. Final Value of Variable After Performing Operations

## Problem

You are given an array of strings `operations`, where each string represents a single operation performed on a variable `X`.

The language allows only four possible operations:

- `"++X"` and `"X++"`: increment `X` by 1
- `"--X"` and `"X--"`: decrement `X` by 1

Initially, `X = 0`.

Return the final value of `X` after performing all operations.

### Example 1

Input: `operations = ["--X","X++","X++"]`
Output: `1`
Explanation:

- Start with `X = 0`
- "--X" → X = -1
- "X++" → X = 0
- "X++" → X = 1

### Example 2

Input: `operations = ["++X","++X","X++"]`
Output: `3`

### Example 3

Input: `operations = ["X++","++X","--X","X--"]`
Output: `0`

### Constraints

- `1 <= operations.length <= 100`
- Each string is one of `"++X"`, `"X++"`, `"--X"`, `"X--"`

---

## Intuition

Each operation either increments or decrements the variable `X` by exactly 1. The actual position of the operator (`++` before or after `X`) does not matter for this problem, because the value is updated immediately either way.

The simplest way is to traverse all operations and adjust the value of `X` depending on whether the operation contains `'+'` or `'-'`.

---

## Approach

1. Initialize the variable `X = 0`.
2. Loop through each operation in the input array:

   - If the operation contains a `'+'` (either `"++X"` or `"X++"`), increment `X`.
   - Otherwise (for `"--X"` or `"X--"`), decrement `X`.

3. After all operations are processed, return the final value of `X`.

This requires only a single pass through the list.

---

## Complexity

**Time Complexity:**
O(n), where n is the number of operations.

**Space Complexity:**
O(1), since only one variable is used.

---

## Code

```python
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if '+' in op:
                x += 1
            else:
                x -= 1
        return x
```

---
