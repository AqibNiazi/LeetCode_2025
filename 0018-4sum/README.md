# 18. 4Sum

## Problem Description

Given an integer array `nums` of length `n`, return an array of all the **unique quadruplets** `[nums[a], nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`
- `a, b, c, and d` are distinct
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in any order.

---

### Example 1

**Input:**
`nums = [1,0,-1,0,-2,2], target = 0`

**Output:**
`[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`

---

### Example 2

**Input:**
`nums = [2,2,2,2,2], target = 8`

**Output:**
`[[2,2,2,2]]`

---

### Constraints

- `1 <= nums.length <= 200`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= target <= 10⁹`

---

## Intuition

The **4Sum** problem extends the concept of **3Sum** by adding one more level of iteration.
We need to find all unique quadruplets whose sum equals the given target.

A brute-force solution would check all possible quadruplets (`O(n⁴)`), which is inefficient.
By **sorting the array** and using **two pointers** inside nested loops, we can reduce it to **O(n³)**.

---

## Approach

1. **Sort the array** — this helps avoid duplicates and enables two-pointer optimization.
2. Iterate through the array with index `i` (for the first number).

   - Skip duplicates for `nums[i]`.

3. For each `i`, iterate with index `j` (for the second number).

   - Skip duplicates for `nums[j]`.

4. Use **two pointers**:

   - `left = j + 1`, `right = n - 1`.
   - Compute `total = nums[i] + nums[j] + nums[left] + nums[right]`.
   - If `total == target`, store the quadruplet and move both pointers.
   - If `total < target`, increment `left`.
   - If `total > target`, decrement `right`.

5. Skip duplicate values for both `left` and `right` to avoid repeated quadruplets.
6. Continue until all combinations are checked.

---

## Code Implementation

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res
```

---

## Complexity Analysis

- **Time Complexity:** `O(n³)`

  - Two nested loops and a two-pointer scan inside.

- **Space Complexity:** `O(1)`

  - In-place operations (excluding result storage).

---
