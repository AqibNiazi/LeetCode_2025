## Problem Description

Given two strings **s** and **t**, return **true** if they are equal when both are typed into empty text editors.
Here, `'#'` represents a _backspace_ character.

If a backspace is applied to an empty string, it stays empty.

### Examples

**Example 1:**

```
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both strings become "ac".
```

**Example 2:**

```
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both strings become "".
```

**Example 3:**

```
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
```

### Constraints

- 1 ≤ s.length, t.length ≤ 200
- s and t contain only lowercase letters and `#`
- Follow-up: Solve in **O(n)** time and **O(1)** space.

---

# Solution

## Intuition

When typing each character of a string, the `'#'` behaves like a backspace:

- It removes the last added character (if any).
- Otherwise, nothing happens.

The problem essentially asks:
**What do the two strings look like after all typing operations?**

A straightforward way is to process each string using a stack-like method where:

- Normal characters get appended.
- `'#'` pops the previous character if the stack is not empty.

After fully processing both strings, we simply compare the results.

This approach gives a clear, simple, and reliable solution.

---

## Approach

1. Define a helper function `build(string)`:

   - Initialize an empty list `stack`.
   - Iterate through each character:

     - If it is `'#'`, pop from stack if stack is not empty.
     - Otherwise, push the character to the stack.

   - Return the final stack.

2. Process both `s` and `t` using `build()`.

3. Compare the final processed lists.

4. If they match, return `True`; otherwise, return `False`.

---

## Time & Space Complexity

- **Time Complexity:** O(n + m)
  Each character from both strings is processed once.

- **Space Complexity:** O(n + m)
  In the worst case, all characters are stored in stacks.

---

## Code

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string: str) -> List[str]:
            stack = []
            for ch in string:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack

        return build(s) == build(t)
```
