# 459. Repeated Substring Pattern

## Problem Description

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

### Examples

**Example 1**

```
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" repeated twice.
```

**Example 2**

```
Input: s = "aba"
Output: false
```

**Example 3**

```
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" repeated four times or "abcabc" repeated twice.
```

### Constraints

- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters only

---

## Solution

### Intuition

If a string is formed by repeating a smaller substring, then:

- The length of that substring must divide the total length of the string.
- Repeating that substring the required number of times should reconstruct the original string exactly.

We only need to check substring lengths up to half of the string length, because a repeating substring cannot be longer than that.

---

### Approach

1. Get the length of the string `n`.
2. Try all possible substring lengths `l` from `n // 2` down to `1`.
3. For each `l`:

   - Check if `l` divides `n`.
   - Extract the substring `s[:l]`.
   - Repeat it `n // l` times.
   - If the constructed string equals the original string, return `True`.

4. If no valid substring works, return `False`.

---

### Python Code

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # A repeating substring cannot be longer than half the string
        for l in range(n // 2, 0, -1):
            if n % l == 0:
                times = n // l
                pattern = s[:l]
                new_str = ""

                while times > 0:
                    new_str += pattern
                    if new_str == s:
                        return True
                    times -= 1
        return False
```

---

### Complexity Analysis

- **Time Complexity:**
  ( O(n^2) )
  In the worst case, building and comparing repeated substrings takes quadratic time.

- **Space Complexity:**
  ( O(n) )
  Extra space is used to build the repeated string.
