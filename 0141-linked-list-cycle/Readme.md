# 141. Linked List Cycle

## Problem Description

Given the head of a singly linked list, determine whether the list contains a cycle.
A cycle exists if a node in the list can be revisited by continuously following the `next` pointers.

The parameter `pos` (used internally in test cases) indicates the index of the node that the tail connects to.
`pos` is not given as input; it only describes how the cycle is formed.

Return **true** if a cycle exists, otherwise return **false**.

### Examples

**Example 1:**
Input: `head = [3,2,0,-4], pos = 1`
Output: `true`
Explanation: Tail connects to index 1.

**Example 2:**
Input: `head = [1,2], pos = 0`
Output: `true`
Explanation: Tail connects to index 0.

**Example 3:**
Input: `head = [1], pos = -1`
Output: `false`
Explanation: No cycle exists.

### Constraints

- The number of nodes is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid linked list index.

### Follow-up

Can you solve it using **O(1)** memory?

---

## Intuition

A naive way to detect a cycle is by storing visited nodes in a set, but that requires extra memory.
To achieve constant space, we use the **Floyd’s Tortoise and Hare** algorithm.

If the list has a cycle:

- A slow pointer (moves 1 step)
- And a fast pointer (moves 2 steps)
  will eventually meet at some node inside the cycle.

If the fast pointer reaches `None`, no cycle exists.

---

## Approach

1. Initialize two pointers:

   - `slow` starts at `head`
   - `fast` starts at `head`

2. Move pointers:

   - `slow = slow.next`
   - `fast = fast.next.next`

3. At any point if `slow == fast`, a cycle exists → return `True`.
4. If `fast` or `fast.next` becomes `None`, there is no cycle → return `False`.

This approach ensures **O(1) space** and **single-pass efficiency**.

---

## Complexity

- **Time Complexity:**
  `O(n)` — in the worst case, both pointers traverse the list.

- **Space Complexity:**
  `O(1)` — only two pointers are used.

---

## Code Implementation

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```
