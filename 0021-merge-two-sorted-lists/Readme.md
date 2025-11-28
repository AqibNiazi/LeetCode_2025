# Merge Two Sorted Lists — LeetCode 21

## 🧩 Problem

You are given the heads of two **sorted linked lists** `list1` and `list2`.
Merge the two lists into **one sorted linked list** by **splicing together** the existing nodes (no new nodes except a dummy helper).
Return the head of the merged list.

---

### **Example 1**

**Input:**
`list1 = [1,2,4]`, `list2 = [1,3,4]`
**Output:**
`[1,1,2,3,4,4]`

### **Example 2**

**Input:**
`list1 = []`, `list2 = []`
**Output:**
`[]`

### **Example 3**

**Input:**
`list1 = []`, `list2 = [0]`
**Output:**
`[0]`

---

### **Constraints**

- Number of nodes in both lists: `0 ≤ n ≤ 50`
- Node values: `-100 ≤ val ≤ 100`
- Both lists are sorted in **non-decreasing** order.

---

## Whiteboard Explanation

Draw-along visual walkthrough:
[https://miro.com/app/board/uXjVJj7ZTxk=/?share_link_id=79193817643](https://miro.com/app/board/uXjVJj7ZTxk=/?share_link_id=79193817643)

---

# 💡 Intuition

We need to merge two **already sorted** linked lists.
The optimal way is to **compare their current nodes**, take the smaller one, and attach it to the merged list.
Continue until one list finishes, then append the remaining nodes.

A **dummy node** helps simplify edge cases and keeps track of the head of the merged list.

---

# 🚀 Approach

1. Create a **dummy node** and set a `tail` pointer to it.
2. While both `list1` and `list2` are non-empty:

   - Compare `list1.val` and `list2.val`
   - Append the smaller node to `tail.next`
   - Move the pointer (`list1` or `list2`) forward
   - Move `tail` forward

3. After loop ends, **one list may still have nodes**

   - Append the leftover list directly

4. Return `dummy.next` (head of merged list)

---

# ⏱️ Complexity

### **Time Complexity:**

[
O(n + m)
]
We traverse each list once.

### **Space Complexity:**

[
O(1)
]
We don’t create new nodes — only rearrange pointers.

---

# 🧠 Code (Python)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
```

---
