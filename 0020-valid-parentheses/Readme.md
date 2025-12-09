# Valid Parentheses – LeetCode 20

## Problem

Given a string `s` containing only the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the string is valid.

A string is considered valid if:

1. Every open bracket has a corresponding closing bracket of the same type.
2. Brackets close in the correct order.
3. Every closing bracket must match the most recent unmatched opening bracket.

**Examples**

| Input      | Output  |
| ---------- | ------- |
| `"()"`     | `true`  |
| `"()[]{}"` | `true`  |
| `"(]"`     | `false` |
| `"([])"`   | `true`  |
| `"([)]"`   | `false` |

**Constraints:**
• `1 <= s.length <= 10^4`
• Contains only `'()[]{}'`

---

## Solution (LeetCode-Post Style)

### Intuition

We need to ensure every closing bracket matches the most recent opening bracket. A **stack** is the perfect data structure for this because it allows us to track brackets in the required LIFO order. Whenever we see a closing bracket, we check if it matches the last pushed opening bracket.

If all brackets match perfectly and the stack is empty at the end, the string is valid.

---

### Approach

1. Create an empty stack.
2. Define a mapping `closeToOpen` that maps each closing bracket to its corresponding opening one.
3. Traverse the string:

   - If the character is an opening bracket, push it onto the stack.
   - If it is a closing bracket:

     - Check if the stack is not empty **and** the top of the stack matches the corresponding opening bracket.

       - If yes, pop the stack.
       - If not, return `False`.

4. After the loop, if the stack is empty, return `True`; otherwise `False`.

---

### Complexity

- **Time Complexity: O(n)**
  We scan the string once.
- **Space Complexity: O(n)**
  In the worst case (all opening brackets), they all go onto the stack.

---

## Code (Python)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # store open brackets
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
```
