# 1544. Make The String Great

### Problem Description

Given a string `s` containing both lowercase and uppercase English letters, a **good** string is one where no two adjacent characters form a bad pair.  
A **bad pair** occurs when:

- `s[i]` and `s[i+1]` are the same letter,
- but one is lowercase and the other is uppercase.

You are allowed to repeatedly remove adjacent bad pairs until the string becomes good.  
Return the resulting good string. The result is guaranteed to be unique.

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


## Intuition

The key observation is that a bad pair is formed when two adjacent characters are the same letter but different cases.
This naturally suggests using a **stack**.
As we iterate through the string:

- If the current character forms a bad pair with the top of the stack, remove the top (bad pair eliminated).
- Otherwise, push the current character.

This mimics the process of repeatedly deleting bad adjacent pairs until the string becomes good.

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


## Time and Space Complexity

- **Time Complexity:** `O(n)`
  Each character is pushed or popped at most once.
- **Space Complexity:** `O(n)`
  In the worst case no removals occur, and the stack holds the entire string.

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
---

# Step-by-step explanation of this solution

Nice — this is a clean stack-based solution for **Make The String Great**. I’ll walk through it line-by-line, explain the helper `lower` function, show why the `if` condition detects a canceling pair (same letter, opposite case), run a concrete example, and finish with complexity and a simpler alternative.

---

## What the code does (one-sentence)

It scans `s` left-to-right, using a stack to remove adjacent letter pairs that are the same alphabetic character but in opposite cases (like `'a'` and `'A'`). The final stack joined into a string is the “good” string.

---

## Code with commentary

```py
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
# Step by Step Explanation
### `lower(c)` helper

* Purpose: return the lowercase version of the character `c`.
* Implementation detail:

  * `ord(c) < ord('a')` checks whether `c` is an uppercase letter (because uppercase letters have smaller ASCII/Unicode code points than lowercase).
  * If uppercase, it converts to lowercase using arithmetic: `chr(ord('a') + ord(c) - ord('A'))`.
  * Otherwise returns `c` (already lowercase).
* Effectively `lower(c)` behaves like Python’s built-in `c.lower()`.

### `stack = []`

* We will push characters into `stack`. When we find a canceling pair (top of stack + current char), we `pop()` instead.

### Main loop `while i < len(s):`

* We process characters one by one from left to right; `i` is the index.

### The `if` condition:

```py
if (stack and stack[-1] != s[i] and lower(stack[-1]) == lower(s[i])):
    stack.pop()
else:
    stack.append(s[i])
```

This checks three things simultaneously:

1. `stack` — ensure the stack is not empty (otherwise `stack[-1]` would be invalid).
2. `stack[-1] != s[i]` — ensure the two characters are not *exactly* the same (if they were identical and same case, they should **not** cancel).
3. `lower(stack[-1]) == lower(s[i])` — ensure that when both are reduced to lowercase, they are the **same letter**.

Taken together: the top-of-stack character and the current character are the **same letter but different cases**. Example: `stack[-1] = 'a'` and `s[i] = 'A'`, or vice versa `'B'` and `'b'`. If so — they cancel, so we `pop()` the stack (removing the previous char) and do not push the current char, effectively removing both.

If the condition is false, we `append` the current character to the stack.

### End

After the loop we `return "".join(stack)` — the characters left form the final “good” string.

---

## Concrete trace (example)

Take `s = "leEeTcOde"` (I’ll use a smaller variant: `s = "aAbBc"`)

Indices and chars: `0:'a' 1:'A' 2:'b' 3:'B' 4:'c'`
Start: `stack = []`

* `i=0`, char `'a'`: stack empty → append `'a'` → `stack = ['a']`.
* `i=1`, char `'A'`: `stack` non-empty, `stack[-1] = 'a' != 'A'`, and `lower('a') == lower('A') == 'a'` → condition true → `stack.pop()` → `stack = []`.
* `i=2`, char `'b'`: stack empty → append `'b'` → `stack = ['b']`.
* `i=3`, char `'B'`: top `'b' != 'B'` and `lower(...)` equal → pop → `stack = []`.
* `i=4`, char `'c'`: append `'c'` → `stack = ['c']`.

Return `"c"`.

So `"aAbBc"` → `"c"` (pairs `'a'/'A'` and `'b'/'B'` removed).

---

## Why this works

* The stack enforces *last-opened, first-closed* — whenever two adjacent characters cancel, it may create a new adjacent pair that should cancel as well; the stack naturally handles that by checking the new top with the next input.
* The condition exactly captures “same letter different case”:

  * `lower(stack[-1]) == lower(s[i])` ensures same letter,
  * `stack[-1] != s[i]` ensures opposite case (because if they were equal as characters, they would be identical case and should not cancel).

---

## Complexity

* Time: **O(n)** where `n = len(s)` — each character is pushed or popped at most once.
* Space: **O(n)** worst-case stack size (e.g., if no cancellations occur).

---

## Small improvements / simpler alternative

* The `lower` helper can be replaced by Python’s built-in `c.lower()` for clarity:

```py
if stack and stack[-1] != c and stack[-1].lower() == c.lower():
    stack.pop()
else:
    stack.append(c)
```

* Another elegant trick: push the *expected canceling counterpart* for each opening-like char, but with case problems it’s simpler to keep above logic.

---

## Edge cases

* Empty string `s = ""` → returns `""`.
* All characters cancel pairwise → returns `""`.
* Non-letter characters are not part of problem constraints; this code assumes only letters (or at least that uppercase/lowercase detection via ord works).

---
