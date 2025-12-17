# 485. Max Consecutive Ones

## Problem Statement

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

### Examples

**Example 1**

```

Input: nums = [1,1,0,1,1,1]
Output: 3

**Example 2**

```

Input: nums = [1,0,1,1,0,1]
Output: 2

### Constraints

- 1 <= nums.length <= 10^5
- nums[i] is either `0` or `1`

### Intuition

While traversing the array, consecutive `1`s form a continuous segment.
If we keep counting `1`s until we hit a `0`, we can track the length of each such segment.
The goal is to find the maximum length among all these segments.

### Approach

- Use two variables:
  - `count` to track the current number of consecutive `1`s.
  - `max_count` to store the maximum consecutive `1`s found so far.
- Traverse the array:
  - If the current element is `1`, increment `count` and update `max_count`.
  - If the current element is `0`, reset `count` to `0`.
- After the loop, return `max_count`.

This approach processes the array in one pass.

## Solution Code

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0

        for i in range(len(nums)):
            if nums[i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count
```

## Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the array.
- **Space Complexity:** O(1), since only constant extra space is used.
