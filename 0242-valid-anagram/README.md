# 242. Valid Anagram

**Difficulty:** Easy  
**Topics:** Hash Table, String, Sorting

---

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

---

### Example 1

**Input:**  
`s = "anagram", t = "nagaram"`  
**Output:**  
`true`

---

### Example 2

**Input:**  
`s = "rat", t = "car"`  
**Output:**  
`false`

---

### Constraints

- `1 <= s.length, t.length <= 5 * 10⁴`
- `s` and `t` consist of lowercase English letters.

---

### Follow-up

What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

---

## Intuition

An anagram means both strings contain the **same characters** with the **same frequency**.  
If two strings are anagrams, sorting both will produce identical results, or counting the occurrences of each character will yield identical frequency maps.

Instead of sorting (which takes O(n log n) time), we can count the frequency of each character using hash maps (dictionaries in Python) for a more optimal O(n) solution.

---

## Approach

1. If the lengths of `s` and `t` differ, they cannot be anagrams — return `False`.
2. Create two dictionaries, `countS` and `countT`, to store character frequencies for `s` and `t`.
3. Iterate through each character:
   - Increment its count in both dictionaries.
4. After populating the dictionaries, compare them:
   - If every character count in `s` matches its corresponding count in `t`, return `True`.
   - Otherwise, return `False`.

This approach ensures we only traverse the strings once and perform constant-time lookups and updates.

---

## Complexity

- **Time Complexity:** `O(n)`  
  We iterate once through both strings of length `n`.

- **Space Complexity:** `O(1)`  
  Although we use two hash maps, the number of possible lowercase English letters is constant (26).  
  Hence, space usage is constant relative to input size.

---

## Code Implementation

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
```

````

---

## Alternative Approaches

### 1. Sorting-Based

Compare sorted versions of `s` and `t`.

```python
return sorted(s) == sorted(t)
```

**Time Complexity:** `O(n log n)`
**Space Complexity:** `O(1)` or `O(n)` depending on sorting implementation.

### 2. Single Hash Map Optimization

Use one dictionary to increment for `s` and decrement for `t`, then check if all counts are zero.
This reduces space and code redundancy.

---

## Follow-Up: Unicode Support

For Unicode strings, we can still use the dictionary approach since Python’s dictionary supports Unicode keys.
No change is required other than ensuring we handle characters beyond the ASCII range properly.
````
