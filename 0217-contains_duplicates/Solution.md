## 💡 Intuition

We need to determine if the array contains any duplicates.
The simplest and most efficient way to track previously seen elements is by using a **HashSet**.
Sets do not allow duplicate values, and lookups in a set are on average `O(1)`.

As we iterate through the array:

- If the current number is already in the set → it’s a duplicate → return `True`.
- Otherwise, we add it to the set and continue checking.

If the loop ends without finding duplicates, we return `False`.

---

## 🚀 Approach

1. Initialize an empty HashSet named `hashset`.
2. Traverse each number `n` in the list `nums`.
3. If `n` exists in `hashset`, return `True` (duplicate found).
4. Otherwise, insert `n` into `hashset`.
5. After the loop, return `False` (all unique).

---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n)` — Each number is checked and inserted once.
- **Space Complexity:** `O(n)` — In the worst case, all elements are stored in the HashSet.

---

## ✅ Code Implementation

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
```

---

## 🧩 Example Walkthrough

**Example:**

```python
nums = [1, 2, 3, 1]
```

**Step-by-step Execution:**

| Step | Element | HashSet Before | Action          | HashSet After |
| ---- | ------- | -------------- | --------------- | ------------- |
| 1    | 1       | `{}`           | Add `1`         | `{1}`         |
| 2    | 2       | `{1}`          | Add `2`         | `{1, 2}`      |
| 3    | 3       | `{1, 2}`       | Add `3`         | `{1, 2, 3}`   |
| 4    | 1       | `{1, 2, 3}`    | Duplicate found | —             |

✅ **Output:** `True`

---

## 🧾 Summary

✅ Uses **HashSet** for O(1) lookups
✅ **Linear Time**, **Linear Space**
✅ Efficient and beginner-friendly approach
