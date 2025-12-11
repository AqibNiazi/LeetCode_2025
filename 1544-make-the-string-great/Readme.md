# 1544. Make The String Great

### Problem Description

Given a string `s` containing both lowercase and uppercase English letters, a **good** string is one where no two adjacent characters form a bad pair.  
A **bad pair** occurs when:

- `s[i]` and `s[i+1]` are the same letter,
- but one is lowercase and the other is uppercase.

You are allowed to repeatedly remove adjacent bad pairs until the string becomes good.  
Return the resulting good string. The result is guaranteed to be unique.

---

### Examples

**Example 1**

```

Input: s = "leEeetcode"
Output: "leetcode"

```

**Example 2**

```

Input: s = "abBAcC"
Output: ""

```

**Example 3**

```

Input: s = "s"
Output: "s"

```

---

## Intuition

The key observation is that a bad pair is formed when two adjacent characters are the same letter but different cases.
This naturally suggests using a **stack**.
As we iterate through the string:

- If the current character forms a bad pair with the top of the stack, remove the top (bad pair eliminated).
- Otherwise, push the current character.

This mimics the process of repeatedly deleting bad adjacent pairs until the string becomes good.

---

## Approach

1. Maintain a stack to hold characters of the gradually cleaned string.
2. For each character in `s`:
   - Compare it with the top of the stack.
   - A bad pair is detected if:
     - Characters are different
     - But they become equal when converted to lowercase
   - If a bad pair is found, pop the stack.
   - Otherwise, push the current character.
3. Join the remaining stack contents to form the final good string.

To check character equivalence in lowercase, use a helper function to convert uppercase to lowercase via ASCII math.

---

## Time and Space Complexity

- **Time Complexity:** `O(n)`
  Each character is pushed or popped at most once.
- **Space Complexity:** `O(n)`
  In the worst case no removals occur, and the stack holds the entire string.

---

## Code Implementation

```python
class Solution:
    def makeGood(self, s: str) -> str:

        def lower(c):
            if ord(c) < ord('a'):
                return chr(ord('a') + ord(c) - ord('A'))
            return c

        stack = []

        i = 0
        while i < len(s):
            if (stack and stack[-1] != s[i] and lower(stack[-1]) == lower(s[i])):
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)
```
