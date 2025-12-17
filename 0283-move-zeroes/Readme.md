# 283. Move Zeroes

## Problem

Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

You must do this **in-place** without making a copy of the array.

### Examples

**Example 1**

```

Input:  nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

**Example 2**

```

Input:  nums = [0]
Output: [0]

```

### Constraints

- 1 <= nums.length <= 10⁴
- -2³¹ <= nums[i] <= 2³¹ - 1

### Solution

## Intuition

All non-zero elements should appear in the same order, just shifted to the front of the array. Zeros should naturally end up at the back.  
This can be done by scanning the array and keeping track of where the next non-zero element should go.

## Approach

- Use two pointers:
  - `l` points to the position where the next non-zero element should be placed.
  - `r` iterates through the array.
- When a non-zero element is found at index `r`, swap it with the element at index `l`.
- Increment `l` after placing a non-zero element.
- By the end, all non-zero elements are at the front in order, and zeros are pushed to the back.

## Solution (Python)

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
```

## Complexity

- **Time Complexity:** O(n)
  Each element is processed once.
- **Space Complexity:** O(1)
  The array is modified in-place without extra space.
