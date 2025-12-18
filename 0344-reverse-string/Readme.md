# 344. Reverse String

## Problem Statement

Write a function that reverses a string.  
The input string is given as an array of characters `s`.

You must do this by modifying the input array **in-place** with **O(1)** extra memory.

---

### Examples

**Example 1**

```

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

```

**Example 2**

```

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

```

---

### Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character

---

## Intuition

To reverse a string in-place, we can swap characters from both ends of the array.  
The first character should swap with the last, the second with the second last, and so on, until we reach the middle.

This avoids using extra space and keeps the operation efficient.

---

## Approach

- Use two pointers:
  - `l` starting from the beginning of the array
  - `r` starting from the end of the array
- While `l < r`:
  - Swap `s[l]` and `s[r]`
  - Move `l` forward and `r` backward
- Stop when the two pointers meet or cross

This modifies the array directly as required.

---

## Solution Code (Python)

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  Each character is visited at most once.

- **Space Complexity:** `O(1)`
  Reversal is done in-place without extra memory.
