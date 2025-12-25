# 796. Rotate String

## Problem Description

Given two strings `s` and `goal`, return `true` if and only if `s` can become `goal` after some number of shifts on `s`.

A shift on `s` consists of moving the leftmost character of `s` to the rightmost position.

### Examples

**Example 1**

```
Input: s = "abcde", goal = "cdeab"
Output: true
```

**Example 2**

```
Input: s = "abcde", goal = "abced"
Output: false
```

### Constraints

- `1 <= s.length, goal.length <= 100`
- `s` and `goal` consist of lowercase English letters

---

## Intuition

If we keep rotating the string `s`, at some point it will either match `goal` or return back to its original form.
If no rotation matches `goal`, then it is not possible.

Another observation is that if `goal` is a rotation of `s`, then `goal` must be a substring of `s + s`.

---

## Approach 1: Brute Force (Simulate Rotations)

### Explanation

- First check if the lengths of `s` and `goal` are equal.
- Rotate `s` one character at a time.
- After each rotation, compare it with `goal`.
- If any rotation matches, return `true`.

### Code

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        for _ in range(len(s)):
            if s == goal:
                return True
            s = s[1:] + s[0]
        return False
```

### Complexity

- **Time Complexity:** `O(n^2)`
  Each rotation takes `O(n)` and we do it `n` times.
- **Space Complexity:** `O(1)` (ignoring string slicing cost)

---

## Approach 2: Optimized (String Concatenation Trick)

### Explanation

- If `goal` is a rotation of `s`, then it must appear inside `s + s`.
- Example:

  - `s = "abcde"`
  - `s + s = "abcdeabcde"`
  - `"cdeab"` is a substring of `"abcdeabcde"`

### Code

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)
```

### Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` for concatenated string

---

## Summary

- Brute force is easy to understand but inefficient.
- The optimized approach is cleaner and more efficient.
- Checking `goal in s + s` is the key insight for this problem.
