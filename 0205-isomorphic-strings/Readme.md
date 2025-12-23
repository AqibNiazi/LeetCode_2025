# 205. Isomorphic Strings

## Problem Description

Given two strings `s` and `t`, determine if they are **isomorphic**.

Two strings are isomorphic if the characters in `s` can be replaced to get `t`, with the following rules:

- Each character must map to exactly one other character.
- The mapping must preserve the order of characters.
- No two different characters can map to the same character.
- A character can map to itself.

## Examples

**Example 1**

```
Input: s = "egg", t = "add"
Output: true
```

**Example 2**

```
Input: s = "foo", t = "bar"
Output: false
```

**Example 3**

```
Input: s = "paper", t = "title"
Output: true
```

---

## Constraints

- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of valid ASCII characters

## Intuition

To ensure the strings are isomorphic, each character in `s` should consistently map to the same character in `t`.

At the same time, we must ensure that:

- One character in `t` is not mapped from multiple characters in `s`.

This means we need **two-way mapping**:

- From `s` to `t`
- From `t` to `s`

If either mapping violates consistency, the strings are not isomorphic.

## Approach

1. Use two hash maps:

   - `mapST` to store mapping from `s` to `t`
   - `mapTS` to store mapping from `t` to `s`

2. Traverse both strings character by character.
3. For each character pair:

   - Check if the mapping already exists and is consistent.
   - If not consistent, return `False`.

4. If all characters satisfy the mapping rules, return `True`.

## Solution (Python)

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True
```

## Complexity Analysis

- **Time Complexity:** `O(n)`
  We traverse the strings once.

- **Space Complexity:** `O(n)`
  Extra space is used for the hash maps.

## Summary

- This problem checks **one-to-one character mapping**.
- Using two hash maps ensures mapping consistency from both directions.
- Efficient and clean solution using linear time.
