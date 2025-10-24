# 189. Rotate Array

## Problem Description

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

---

### Example 1

**Input:**
`nums = [1,2,3,4,5,6,7], k = 3`

**Output:**
`[5,6,7,1,2,3,4]`

**Explanation:**

- Rotate 1 step to the right: `[7,1,2,3,4,5,6]`
- Rotate 2 steps to the right: `[6,7,1,2,3,4,5]`
- Rotate 3 steps to the right: `[5,6,7,1,2,3,4]`

---

### Example 2

**Input:**
`nums = [-1,-100,3,99], k = 2`

**Output:**
`[3,99,-1,-100]`

**Explanation:**

- Rotate 1 step to the right: `[99,-1,-100,3]`
- Rotate 2 steps to the right: `[3,99,-1,-100]`

---

### Constraints

- `1 <= nums.length <= 10⁵`
- `-2³¹ <= nums[i] <= 2³¹ - 1`
- `0 <= k <= 10⁵`

---

### Follow-up

Try to come up with as many solutions as possible. There are at least three different ways to solve this problem:

- Using extra space
- Using reversal in-place
- Using cyclic replacements

Could you do it **in-place with O(1) extra space**?

---

## Intuition

When rotating an array to the right by `k` steps, the last `k` elements move to the beginning, while the rest shift to the right.
A direct approach would use an extra array, but the challenge is to perform the rotation **in-place** with **O(1)** extra space.

We can achieve this efficiently using the **reversal algorithm**:

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining elements.

---

## Approach

1. Compute `k = k % len(nums)` to handle cases where `k` is larger than the array length.
2. Reverse the **entire array**.
3. Reverse the **first `k` elements**.
4. Reverse the **remaining elements** from `k` to the end.
5. The array is now rotated in-place with no extra space.

---

## Code Implementation

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        l, r = 0, len(nums) - 1

        # Reverse entire array
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        # Reverse first k elements
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        # Reverse remaining elements
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)`

  - Each element is reversed exactly once (three reversals total).

- **Space Complexity:** `O(1)`

  - The rotation is done in-place with no additional data structures.

---

## Key Takeaways

- Reversing segments of the array is an elegant way to rotate it efficiently.
- Handles large `k` values using modulo operation.
- In-place algorithm ensures minimal memory usage.
