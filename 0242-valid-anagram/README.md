# 242. Valid Anagram

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

### Example 1

**Input:**
`s = "anagram", t = "nagaram"`

**Output:**
`true`

### Example 2

**Input:**
`s = "rat", t = "car"`

**Output:**
`false`

## Constraints

* `1 <= s.length, t.length <= 5 * 10⁴`
* `s` and `t` consist of lowercase English letters.


## Follow-up

What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Intuition

An anagram means both strings contain the **same characters** with the **same frequency**.

If two strings are anagrams:

* They must have equal length.
* Every character must appear the same number of times in both strings.

Instead of sorting (which takes `O(n log n)` time), we can count character frequencies using hash maps (Python dictionaries) to achieve an `O(n)` time solution.


# Main Approach — Two Dictionary Method

## Approach

1. If the lengths of `s` and `t` differ, return `False`.
2. Create two dictionaries:

   * `countS` → stores frequency of characters in `s`
   * `countT` → stores frequency of characters in `t`
3. Traverse both strings simultaneously and update counts.
4. Compare both dictionaries.
5. If they are equal, return `True`; otherwise, return `False`.


## Code Implementation (Two Dictionaries)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
```


## Complexity Analysis

* **Time Complexity:** `O(n)`
  We iterate once through both strings.

* **Space Complexity:** `O(1)`
  Since only 26 lowercase letters exist, dictionary size is bounded.


# Alternative Approach — One Dictionary (Optimized)

Instead of maintaining two dictionaries, we can use **one hash map**.

### Idea:

* Increment counts for characters in `s`.
* Decrement counts for characters in `t`.
* If any count becomes negative or a character doesn’t exist → not an anagram.

This reduces extra space usage and avoids dictionary comparison at the end.


## Code Implementation (Single Dictionary)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Subtract counts using t
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        return True
```


## Why This Is Slightly Better

* Uses only **one dictionary**
* No final dictionary comparison
* Slightly cleaner logic
* Same `O(n)` time complexity


# Sorting-Based Approach (Less Optimal)

```python
return sorted(s) == sorted(t)
```

### Complexity

* **Time Complexity:** `O(n log n)`
* **Space Complexity:** Depends on sorting implementation

This is simpler but slower due to sorting.


# Follow-Up: Unicode Support

If inputs contain Unicode characters:

* The dictionary-based solution still works.
* Python dictionaries support Unicode keys.
* Space complexity becomes `O(k)` where `k` is the number of unique characters.

No structural change is required — only ensure you're not relying on fixed-size arrays of 26 characters.


# Final Comparison

| Approach         | Time       | Space | Recommended      |
| ---------------- | ---------- | ----- | ---------------- |
| Two Dictionaries | O(n)       | O(1)  | ✅ Main           |
| One Dictionary   | O(n)       | O(1)  | ⭐ More Optimized |
| Sorting          | O(n log n) | O(1)  | ❌ Slower         |

