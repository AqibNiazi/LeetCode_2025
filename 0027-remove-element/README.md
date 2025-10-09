# 27. Remove Element

**Solved**
**Easy**

---

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place.
The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` as `k`.
To get accepted, you need to do the following:

- Change the array `nums` such that the first `k` elements contain the elements which are not equal to `val`.
- The remaining elements of `nums` are not important.
- Return `k`.

---

### Example 1

**Input:**
`nums = [3,2,2,3]`, `val = 3`
**Output:**
`2, nums = [2,2,_,_]`
**Explanation:**
Your function should return `k = 2`, with the first two elements of `nums` being `2`.

---

### Example 2

**Input:**
`nums = [0,1,2,2,3,0,4,2]`, `val = 2`
**Output:**
`5, nums = [0,1,4,0,3,_,_,_]`
**Explanation:**
Your function should return `k = 5`, with the first five elements of `nums` being `[0,1,4,0,3]`.

---

### Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

---

## Solution Explanation

### Intuition

We need to remove all occurrences of `val` from the array **in-place**, without using extra memory.
Instead of physically deleting elements (which would require shifting), we overwrite the unwanted elements by compacting valid ones toward the start of the array.

This can be efficiently done using a **two-pointer technique**:

- One pointer (`i`) iterates through all elements.
- Another pointer (`k`) marks the next available position to place a valid element.

---

### Approach

1. Initialize `k = 0` to track the position for valid (non-`val`) elements.
2. Loop through each element `nums[i]`.
3. If `nums[i] != val`, place it at index `k` and increment `k`.
4. After finishing the loop, the first `k` elements of `nums` represent the final array without `val`.
5. Return `k`.

---

### Code Implementation

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
```

---

### Example Walkthrough

**Input:**
`nums = [3,2,2,3], val = 3`

**Process:**

| i   | nums[i] | Action                    | Updated nums | k   |
| --- | ------- | ------------------------- | ------------ | --- |
| 0   | 3       | Skip (equal to val)       | [3,2,2,3]    | 0   |
| 1   | 2       | Keep → place at `nums[0]` | [2,2,2,3]    | 1   |
| 2   | 2       | Keep → place at `nums[1]` | [2,2,2,3]    | 2   |
| 3   | 3       | Skip (equal to val)       | [2,2,2,3]    | 2   |

**Output:**
`k = 2`, `nums = [2,2,_,_]`

---

### Complexity Analysis

- **Time Complexity:** `O(n)` — Each element is processed once.
- **Space Complexity:** `O(1)` — All operations are done in-place.

---
