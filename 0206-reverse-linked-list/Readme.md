# 🔄 Reverse Linked List — LeetCode Problem & Solution

## 📘 Problem

Given the head of a singly linked list, **reverse the list**, and return the reversed list.

---

### **Example 1**

**Input:**
`head = [1,2,3,4,5]`
**Output:**
`[5,4,3,2,1]`

---

### **Example 2**

**Input:**
`head = [1,2]`
**Output:**
`[2,1]`

---

### **Example 3**

**Input:**
`head = []`
**Output:**
`[]`

---

### **Constraints**

* Number of nodes: **0 to 5000**
* Node values: **–5000 to 5000**

---

### **Follow-up**

A linked list can be reversed **iteratively** or **recursively**.
Could you implement both?

---

# 🎥 Whiteboard Explanation

Visual illustration of how the pointers move during reversal:

👉 **[Click here to view the whiteboard explanation](https://miro.com/app/board/uXjVJkXGwEU=/?share_link_id=780075317352)**

---

# ✅ Solution

## 🧠 Intuition

The idea is to reverse the direction of every `next` pointer in the list.
To avoid losing track of nodes, we store the next node temporarily, flip the pointer, and move forward.

---

## 🚀 Approach (Iterative)

We use three pointers:

| Pointer     | Role                                           |
| ----------- | ---------------------------------------------- |
| `prev`      | Points to the previous node (initially `None`) |
| `curr`      | Points to the current node                     |
| `next_temp` | Stores the next node before reversing          |

### Steps:

1. Initialize `prev = None`, `curr = head`.
2. While `curr` exists:

   * Store `curr.next` in `next_temp`.
   * Reverse the pointer.
   * Move `prev` forward.
   * Move `curr` forward.
3. Return `prev` (new head).

---

## 🧩 Iterative Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            new_temp = curr.next   # Save next node
            curr.next = prev       # Reverse pointer
            prev = curr            # Move prev forward
            curr = new_temp        # Move curr forward

        return prev
```

---

## 🔁 Recursive Solution (Follow-up)

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
```

---

## ⏱️ Complexity

### **Time Complexity**

[
O(n)
]
Each node is processed once.

---

### **Space Complexity**

* **Iterative:**
  [
  O(1)
  ]

* **Recursive:**
  [
  O(n)
  ]
  Due to stack frames.

---
