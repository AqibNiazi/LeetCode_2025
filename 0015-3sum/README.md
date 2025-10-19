# 15. 3Sum

## Problem Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`, `i != k`, and `j != k`, and
- `nums[i] + nums[j] + nums[k] == 0`.

The solution set must not contain **duplicate triplets**.

---

### Example 1

**Input:**
`nums = [-1,0,1,2,-1,-4]`

**Output:**
`[[-1,-1,2],[-1,0,1]]`

**Explanation:**

- `nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0`
- `nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0`
- `nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0`

The distinct triplets are `[-1,0,1]` and `[-1,-1,2]`.
Order of triplets and elements does not matter.

---

### Example 2

**Input:**
`nums = [0,1,1]`

**Output:**
`[]`

**Explanation:**
No combination of three numbers adds up to `0`.

---

### Example 3

**Input:**
`nums = [0,0,0]`

**Output:**
`[[0,0,0]]`

**Explanation:**
Only one possible triplet sums up to `0`.

---

### Constraints

- `3 <= nums.length <= 3000`
- `-10⁵ <= nums[i] <= 10⁵`

---

## Intuition

The problem asks for all unique triplets that sum to zero.
A brute-force approach would check all triplets (`O(n³)`), but we can do better.

By **sorting** the array, we can fix one element and then use the **two-pointer** technique to efficiently find the other two elements that complete the triplet. Sorting also helps in **skipping duplicates** easily.

---

## Approach

1. **Sort** the array to simplify duplicate handling and enable the two-pointer approach.
2. Iterate through each number `a` in `nums` using index `i`:

   - If `a > 0`, break (since all later numbers are positive, sum cannot be 0).
   - Skip duplicate values for `a` to avoid repeating triplets.

3. Initialize two pointers:

   - `l = i + 1` (left pointer)
   - `r = len(nums) - 1` (right pointer)

4. Calculate `threeSum = a + nums[l] + nums[r]`:

   - If `threeSum > 0`, decrement `r` to reduce the sum.
   - If `threeSum < 0`, increment `l` to increase the sum.
   - If `threeSum == 0`, append the triplet to the result and move both pointers.
   - Skip duplicate elements for `l` to ensure unique triplets.

5. Return all stored triplets.

---

## Code Implementation

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
```

---

## Complexity Analysis

- **Time Complexity:** `O(n²)` — For each element, the two-pointer search runs in linear time.
- **Space Complexity:** `O(1)` — Only uses constant extra space (excluding output list).
