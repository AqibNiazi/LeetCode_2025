# 1754. Largest Merge Of Two Strings

## Problem Description

You are given two strings `word1` and `word2`. You want to construct a string `merge` using the following rules:

- If `word1` is non-empty, you can take its **first character** and append it to `merge`, then remove it from `word1`
- If `word2` is non-empty, you can take its **first character** and append it to `merge`, then remove it from `word2`

Return the **lexicographically largest** merge you can construct.

## Examples

### Example 1

**Input**

```id="e1"
word1 = "cabaa", word2 = "bcaaa"
```

**Output**

```id="e2"
"cbcabaaaaa"
```

### Example 2

**Input**

```id="e3"
word1 = "abcabc", word2 = "abdcaba"
```

**Output**

```id="e4"
"abdcabcabcaba"
```

## Constraints

- `1 <= word1.length, word2.length <= 3000`
- Strings contain only lowercase English letters

# Intuition

At each step, we must decide:

👉 Should we pick from `word1` or `word2`?

A simple comparison of first characters is **not enough** because:

- If characters are equal, future characters determine which choice is better

👉 So instead of comparing just characters, we compare **remaining substrings**

### Greedy Insight

Always choose the string whose **remaining part is lexicographically larger**

# Approach (Two Pointers + Greedy)

1. Initialize two pointers:
   - `i = 0` for `word1`
   - `j = 0` for `word2`

2. While both strings still have characters:
   - Compare `word1[i:]` and `word2[j:]`
   - If `word1[i:] > word2[j:]`:
     - Append `word1[i]` to result
     - Move `i++`

   - Else:
     - Append `word2[j]`
     - Move `j++`

3. Append remaining characters from either string

4. Return the final merged string

# Solution Code

```python id="c1"
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = []

        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                result.append(word1[i])
                i += 1
            else:
                result.append(word2[j])
                j += 1

        # Append remaining parts
        result.append(word1[i:])
        result.append(word2[j:])

        return "".join(result)
```

# Complexity Analysis

- **Time Complexity:** `O(n^2)`
  - Due to substring comparisons (`word1[i:] > word2[j:]`)

- **Space Complexity:** `O(n + m)`
  - For storing result

# Key Takeaways

- This is a **greedy problem**
- Always compare **remaining substrings**, not just characters
- Two pointers help simulate the merge process efficiently
- Important pattern for:
  - Lexicographical optimization problems
  - String merging strategies
