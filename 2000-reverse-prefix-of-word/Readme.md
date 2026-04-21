# 2000. Reverse Prefix of Word

## Problem Description

Given a **0-indexed string** `word` and a character `ch`, reverse the segment of `word` that starts at index `0` and ends at the **first occurrence** of `ch` (inclusive).

- If `ch` does not exist in `word`, return the original string.

## 🔍 Examples

### Example 1

**Input**

```id="e1"
word = "abcdefd", ch = "d"
```

**Output**

```id="e2"
"dcbaefd"
```

**Explanation**
First occurrence of `"d"` is at index `3`. Reverse substring `[0...3]`.

### Example 2

**Input**

```id="e3"
word = "xyxzxe", ch = "z"
```

**Output**

```id="e4"
"zxyxxe"
```

### Example 3

**Input**

```id="e5"
word = "abcd", ch = "z"
```

**Output**

```id="e6"
"abcd"
```

## Constraints

- `1 <= word.length <= 250`
- `word` consists of lowercase English letters
- `ch` is a lowercase English letter

# Approach 1: String Slicing

## Intuition

Python provides powerful slicing.

👉 Once we find the index of `ch`, we can:

- Reverse the prefix using slicing
- Append the remaining string

## Approach

1. Find the index of first occurrence of `ch` using `find()`
2. If `ch` is not found → return original string
3. Reverse substring from `0 → index`
4. Append remaining part of string

## Code

```python id="c1"
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word
        return word[index::-1] + word[index+1:]
```

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Finding index + slicing

- **Space Complexity:** `O(n)`
  - New string is created

# Approach 2: Two Pointers (In-place Simulation)

## Intuition

Instead of creating new strings, we can:

- Convert string → list (mutable)
- Reverse the prefix using **two pointers**
- Convert back to string

👉 This mimics in-place reversal.

## Approach

1. Convert string into list
2. Traverse to find first occurrence of `ch`
3. If not found → return original string
4. Use two pointers:
   - `l = 0`, `r = index`
   - Swap elements while `l < r`

5. Convert list back to string

## Code

```python id="c2"
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)
        index = -1

        for i in range(len(word_list)):
            if word_list[i] == ch:
                index = i
                break

        if index == -1:
            return word

        l, r = 0, index
        while l < r:
            word_list[l], word_list[r] = word_list[r], word_list[l]
            l += 1
            r -= 1

        return "".join(word_list)
```

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - One pass to find index + one pass to reverse

- **Space Complexity:** `O(n)`
  - List conversion

# Key Takeaways

- **String slicing** is concise and Pythonic
- **Two pointers** give better control and are language-independent
- This is a classic example of:
  - String manipulation
  - Two-pointer reversal pattern
