# Remove Nth Node From End of List — LeetCode #19

## Problem Summary

Given the head of a singly linked list, remove the n-th node from the end of the list and return the updated head.

### Examples

**Example 1**
Input: `[1,2,3,4,5]`, n = 2
Output: `[1,2,3,5]`

**Example 2**
Input: `[1]`, n = 1
Output: `[]`

**Example 3**
Input: `[1,2]`, n = 1
Output: `[1]`

### Constraints

- 1 ≤ list size ≤ 30
- 0 ≤ Node.val ≤ 100
- 1 ≤ n ≤ list size

---

## Intuition

To remove the n-th node from the end efficiently, we avoid calculating the total length of the list. Using two pointers spaced `n` nodes apart allows us to identify the correct node in a single pass.

---

## Approach

1. Create a dummy node pointing to the head to handle edge cases such as removing the first node.
2. Move the `right` pointer `n` steps ahead.
3. Move both pointers together until `right` reaches the end.
4. At this point, `left.next` is the node to remove. Adjust the pointer to skip this node.
5. Return `dummy.next` as the new head of the list.

---

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Code Implementation

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right pointer n steps ahead
        while n > 0:
            right = right.next
            n -= 1

        # Move both pointers
        while right:
            left = left.next
            right = right.next

        # Remove the target node
        left.next = left.next.next

        return dummy.next
```

---
