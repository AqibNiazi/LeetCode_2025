# 0680. Valid Palindrome II

## Problem Statement

Given a string `s`, return `true` if `s` can be a palindrome after deleting at most one character from it.

### Example 1:

```
Input: s = "aba"
Output: true
```

### Example 2:

```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

### Example 3:

```
Input: s = "abc"
Output: false
```

### Constraints:

- `1 <= s.length <= 10⁵`
- `s` consists of lowercase English letters.

---

## Intuition

When checking if a string is a palindrome, we compare characters from both ends toward the center.
If all characters match, it’s already a palindrome.
However, if we find a mismatch, we have one chance to skip either the left or right character and check if the rest forms a palindrome.

---

## Approach

1. Use two pointers:

   - `l` (left) starts at index `0`.
   - `r` (right) starts at index `len(s) - 1`.

2. Compare characters while `l < r`.

3. If `s[l] != s[r]`, there are two possible skips:

   - Skip the left character → `s[l+1:r+1]`
   - Skip the right character → `s[l:r]`

4. If either of these substrings is a palindrome, return `True`.

5. If no mismatches occur, the string is already a palindrome, so return `True`.

---

## Complexity Analysis

- **Time Complexity:** `O(n)` — Each character is compared at most once.
- **Space Complexity:** `O(1)` — Constant space used for two pointers.

---

## Code Implementation

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l, r = l + 1, r - 1
        return True
```

---

## Example Walkthrough

### Example: `s = "abca"`

| Step | l   | r   | s[l] | s[r] | Action                                       |
| ---- | --- | --- | ---- | ---- | -------------------------------------------- |
| 1    | 0   | 3   | 'a'  | 'a'  | Match → move inward                          |
| 2    | 1   | 2   | 'b'  | 'c'  | Mismatch → try skipping                      |
|      |     |     |      |      | Check `"ca"` and `"ab"`                      |
|      |     |     |      |      | Skipping `'c'` makes `"aba"` → palindrome ✅ |

Result: `True`

---

## Summary

- Uses **two-pointer** technique
- Efficiently checks both skip possibilities
- Runs in **O(n)** time and **O(1)** space
- Works for strings up to length `10⁵`
