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

## Line-by-line explanation

1. `dummy = ListNode(0, head)`

   - Create a new node `dummy` whose `next` points to the original `head`.
   - This simplifies deletion when the node to remove is the first node (head). After deletion we will return `dummy.next` (the possibly new head).

2. `left = dummy`

   - `left` is a pointer that will eventually sit **just before** the node we want to remove. We start it at `dummy` so it can move forward safely even when the head must be removed.

3. `right = head`

   - `right` is a pointer that will run ahead of `left` by `n` nodes. Starting it at `head` makes the initial gap calculation easier.

4. `while n > 0: right = right.next; n -= 1`

   - Move `right` forward `n` times. After this loop `right` is `n` nodes ahead of `left.next` (or, equivalently, `right` is `n` nodes ahead of `head` because `left` is at `dummy`).
   - Important: if `n` equals the list length, `right` becomes `None` after this loop — that fact is used to remove the head later.

5. `while right: left = left.next; right = right.next`

   - Move both pointers forward one step at a time until `right` reaches the end (`None`). Because `right` started `n` nodes ahead, when `right` becomes `None`, `left` will be exactly **one node before** the node that must be removed.
   - Invariant: after each iteration, the gap between `right` and `left.next` remains `n`.

6. `left.next = left.next.next`

   - `left.next` is the node to remove. This line bypasses it by pointing `left.next` to the node after the one to remove, effectively deleting it from the chain.

7. `return dummy.next`

   - Return the head of the updated list. Using `dummy.next` handles both normal cases and the situation where the original head was removed.

---

## Visual walkthrough — example

List: `[1 → 2 → 3 → 4 → 5]`, `n = 2`
Goal: remove the 2nd node from the end → remove node with value `4`.

Initial pointers:

```
dummy(0) → 1 → 2 → 3 → 4 → 5 → None
 left
 right
```

After `dummy` and pointers set:

- `left` → `dummy`
- `right` → `head` (node 1)

Step A — advance `right` by `n=2`:

- 1st move: `right` → node 2 (n becomes 1)
- 2nd move: `right` → node 3 (n becomes 0)

Now:

```
dummy → 1 → 2 → 3 → 4 → 5 → None
 left        right
(dummy)      (3)
```

(`right` is 2 nodes ahead of `left.next`, which is node 1)

Step B — move both until `right` is None:

- Iteration 1: `left` → node 1, `right` → node 4
- Iteration 2: `left` → node 2, `right` → node 5
- Iteration 3: `left` → node 3, `right` → None

Now `left` is at node 3, and `left.next` is node 4 — the node we must remove.

Step C — remove:
`left.next = left.next.next` makes node 3 point to node 5:

```
dummy → 1 → 2 → 3 → 5 → None
```

Return `dummy.next` → head of updated list `[1,2,3,5]`.

---

## Edge cases

- **Remove the head** (e.g. list `[1,2,3]`, `n=3`):
  After moving `right` `n` steps it becomes `None`. The second `while` loop does not run, `left` remains `dummy`, and `left.next` is the original head — so `left.next = left.next.next` removes the head correctly. Returning `dummy.next` returns the new head.

- **Single-node list** (`[1]`, `n=1`):
  Same as above — result is an empty list (`dummy.next` becomes `None`).

- The code assumes `1 ≤ n ≤ size`, which is guaranteed by the problem statement.

---

## Why this works (intuition recap)

- Keep a `right` pointer `n` steps ahead of `left.next`. When `right` hits the end, `left.next` is exactly the n-th node from the end. Using a `dummy` makes deletion simple even when the head is removed. Only a single pass after the initial advance is required, so the solution is O(n) time and O(1) extra space.

---

## Complexity

- **Time:** O(sz) — we traverse each node at most a constant number of times.
- **Space:** O(1) — only a few pointers and one dummy node used.

---
