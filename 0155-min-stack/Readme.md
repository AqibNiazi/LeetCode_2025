# Min Stack (LeetCode 155)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

You must implement all operations in O(1) time.

---

## Problem Description

Implement the `MinStack` class:

- `MinStack()` initializes the stack object
- `push(int val)` pushes the element `val` onto the stack
- `pop()` removes the top element
- `top()` returns the top element
- `getMin()` returns the minimum element in the stack

All operations must run in constant time.

### Example

Input

```
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```

Output

```
[null,null,null,null,-3,null,0,-2]
```

Explanation

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // returns -3
minStack.pop();
minStack.top();    // returns 0
minStack.getMin(); // returns -2
```

Constraints:

- -2^31 <= val <= 2^31 - 1
- `pop`, `top`, and `getMin` will always be called on non-empty stacks
- Up to 3 \* 10^4 calls can be made

---

# Solution

Below is the solution explained in the standard LeetCode post format.

---

## Intuition

A normal stack supports push, pop, and top easily, but retrieving the minimum in O(1) time requires an additional idea.
If we scan the stack for the minimum each time, it becomes O(n), which violates the constraints.

To solve this, we maintain another stack that always stores the minimum value at each level of the main stack.
Whenever we push a new value, we also push the minimum of the new value and the previous minimum.
This ensures that the top of the `minStack` always represents the current minimum.

---

## Approach

We use two stacks:

1. `stack`: stores all the actual values
2. `minStack`: stores the minimum value so far at each push

Operations:

- **push(val)**
  Push value onto `stack`.
  Push `min(val, current_min)` onto `minStack`.

- **pop()**
  Pop from both `stack` and `minStack`.

- **top()**
  Return the top of `stack`.

- **getMin()**
  Return the top of `minStack`.

Since every operation touches only the top of the stacks, all operations run in constant time.

---

## Time Complexity

- Push: O(1)
- Pop: O(1)
- Top: O(1)
- GetMin: O(1)

## Space Complexity

- O(n) for storing values and the running minimum for each element.

---

# Code

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
```

---

# Testcase

```
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Expected Output:
[null,null,null,null,-3,null,0,-2]
```

---
