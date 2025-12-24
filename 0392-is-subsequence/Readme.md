# 92. Is Subsequence

## Problem Statement

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence is formed by deleting some (or none) characters from the original string without changing the relative order of the remaining characters.

### Examples

**Example 1**

```

Input: s = "abc", t = "ahbgdc"
Output: true

```

**Example 2**

```

Input: s = "axc", t = "ahbgdc"
Output: false

```

### Constraints

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist of lowercase English letters only

---

## Solution

### Intuition

To check if `s` is a subsequence of `t`, we need to verify that all characters of `s` appear in `t` **in the same order**, though not necessarily consecutively.

We can use two pointers:

- One pointer for `s`
- One pointer for `t`

We move through `t` and try to match characters from `s` in order.

---

### Approach

1. Initialize two pointers `i` and `j` at `0`, pointing to `s` and `t` respectively.
2. Traverse both strings:
   - If `s[i] == t[j]`, move pointer `i` forward.
   - Always move pointer `j` forward.
3. If pointer `i` reaches the end of `s`, it means all characters of `s` were found in order.

---

### Code

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
```

### Complexity Analysis

**Time Complexity:** `O(n)`
Where `n` is the length of string `t`.

**Space Complexity:** `O(1)`
No extra space is used.
