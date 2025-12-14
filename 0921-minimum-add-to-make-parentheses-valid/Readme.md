# 921. Minimum Add to Make Parentheses Valid

## Problem Description

A parentheses string is valid if and only if:

- It is the empty string, or
- It can be written as `AB` (A concatenated with B), where both A and B are valid strings, or
- It can be written as `(A)`, where A is a valid string.

You are given a parentheses string `s`.  
In one move, you can insert a parenthesis `'('` or `')'` at any position of the string.

Return the **minimum number of moves** required to make the string valid.

---

## Examples

**Example 1**

```

Input: s = "())"
Output: 1

```

**Example 2**

```

Input: s = "((("
Output: 3

```

---

## Constraints

- `1 <= s.length <= 1000`
- `s[i]` is either `'('` or `')'`

---

## Intuition

To make the string valid:

- Every closing parenthesis `')'` must have a matching opening parenthesis `'('` before it.
- Every opening parenthesis `'('` must eventually be closed by a `')'`.

While traversing the string:

- If we see `'('`, we expect a `')'` later.
- If we see `')'` without a matching `'('`, we must insert an opening parenthesis.

At the end, any unmatched `'('` will need closing parentheses to become valid.

---

## Approach

1. Keep a counter `open_cnt` to track unmatched `'('`.
2. Keep a variable `res` to count required insertions.
3. Traverse the string character by character:
   - If the character is `'('`, increment `open_cnt`.
   - If the character is `')'`:
     - Decrement `open_cnt`.
     - If `open_cnt` becomes negative, it means we have an extra `')'`:
       - Insert a `'('` (increment `res`)
       - Reset `open_cnt` to `0`
4. After traversal, any remaining `open_cnt` represents unmatched `'('` that need `')'`.
5. Return `res + open_cnt`.

---

## Solution (Python)

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0   # count of unmatched '('
        res = 0        # number of insertions needed

        for c in s:
            if c == "(":
                open_cnt += 1
            else:  # c == ')'
                open_cnt -= 1
                if open_cnt < 0:
                    # extra ')', insert '('
                    res += 1
                    open_cnt = 0

        # remaining '(' need ')'
        return res + open_cnt
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  We traverse the string once.

- **Space Complexity:** `O(1)`
  Only constant extra space is used.

---
