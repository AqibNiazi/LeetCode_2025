# 876. Middle of the Linked List

## Problem Description

Given the head of a singly linked list, return the **middle node** of the linked list.

If there are **two middle nodes**, return the **second** one.

---

### Example 1

**Input:**
`head = [1,2,3,4,5]`

**Output:**
`[3,4,5]`

**Explanation:**
The middle node is node with value **3**.

---

### Example 2

**Input:**
`head = [1,2,3,4,5,6]`

**Output:**
`[4,5,6]`

**Explanation:**
There are two middle nodes (values 3 and 4).
We return the **second** middle node, which is 4.

---

### Constraints

- Number of nodes: `1 <= n <= 100`
- Node values: `1 <= Node.val <= 100`

---

## Intuition

To find the middle node efficiently, we can use the classic **two-pointer technique**. If we move one pointer twice as fast as the other, the slower pointer will reach the middle when the fast one reaches the end.

This avoids counting the nodes first and gives an elegant one-pass solution.

---

## Approach

1. Initialize two pointers:

   - `slow` moves one step at a time
   - `fast` moves two steps at a time

2. Traverse the list until `fast` reaches the end.
3. When the loop ends, `slow` will be at the **middle node**.

   - If the list has two middle nodes, this method naturally returns the **second** one.

4. Return the `slow` pointer.

---

## Code Implementation

```python

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)`

  - We traverse the list once using two pointers.

- **Space Complexity:** `O(1)`

  - Uses only constant extra space.
