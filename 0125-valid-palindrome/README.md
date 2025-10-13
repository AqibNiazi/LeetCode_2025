# 125. Valid Palindrome

**Difficulty:** Easy  
**Topics:** Two Pointers, String

---

## Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.  
Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

### Example 1

**Input:**  
`s = "A man, a plan, a canal: Panama"`  
**Output:**  
`true`  
**Explanation:**  
After cleaning, the string becomes `"amanaplanacanalpanama"`, which reads the same backward.

---

### Example 2

**Input:**  
`s = "race a car"`  
**Output:**  
`false`  
**Explanation:**  
After cleaning, the string becomes `"raceacar"`, which is not a palindrome.

---

### Example 3

**Input:**  
`s = " "`  
**Output:**  
`true`  
**Explanation:**  
After removing non-alphanumeric characters, the string is empty `""`, which is a palindrome.

---

### Constraints

- `1 <= s.length <= 2 * 10⁵`
- `s` consists only of printable ASCII characters.

---

## Intuition

A palindrome reads the same forward and backward.  
However, in this problem, we must **ignore cases** and **non-alphanumeric characters**.

So, the idea is to compare characters from both ends — moving inward — and only consider valid alphanumeric characters.  
If all corresponding pairs match (case-insensitive), the string is a palindrome.

---

## Approach

1. Initialize two pointers:
   - `l` at the start of the string.
   - `r` at the end of the string.
2. While `l < r`:
   - Move `l` forward until it points to an alphanumeric character.
   - Move `r` backward until it points to an alphanumeric character.
   - Compare the lowercase versions of both characters.
     - If they differ, return `False`.
   - Move both pointers inward (`l += 1`, `r -= 1`).
3. If the entire loop completes without mismatches, return `True`.

We also define a helper function `alphaNum()` to manually check if a character is alphanumeric using ASCII values, which avoids using built-in methods and maintains full control over validation.

---

## Complexity

- **Time Complexity:** `O(n)`  
  Each character is checked at most once.

- **Space Complexity:** `O(1)`  
  We only use pointers and a few variables — no additional data structures.

---

## Code Implementation

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
```

---

## Example Walkthrough

**Input:**
`s = "A man, a plan, a canal: Panama"`

| Step | l   | r   | s[l]       | s[r] | Comparison  | Result   |
| ---- | --- | --- | ---------- | ---- | ----------- | -------- |
| 1    | 0   | 29  | 'A'        | 'a'  | 'a' == 'a'  | continue |
| 2    | 1   | 28  | ' ' (skip) | -    | -           | move l   |
| 3    | 2   | 27  | 'm'        | 'm'  | match       | continue |
| ...  | ... | ... | ...        | ...  | ...         | ...      |
| End  | -   | -   | -          | -    | All matched | ✅ True  |

**Output:** `True`

---

## Summary

This two-pointer approach efficiently checks whether a string is a palindrome by ignoring irrelevant characters and case differences.
It achieves optimal linear time with constant space, making it suitable for very long strings.
