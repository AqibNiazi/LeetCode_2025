# 1929. Concatenation of Array

## Problem Statement

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where:

- `ans[i] == nums[i]`
- `ans[i + n] == nums[i]` for `0 <= i < n`

Specifically, `ans` is the concatenation of two `nums` arrays.

Return the array `ans`.

---

## Example 1

```
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation:
ans = [nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]
ans = [1,2,1,1,2,1]
```

## Example 2

```
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation:
ans = [nums[0], nums[1], nums[2], nums[3], nums[0], nums[1], nums[2], nums[3]]
ans = [1,3,2,1,1,3,2,1]
```

---

## Constraints

- `n == nums.length`
- `1 <= n <= 1000`
- `1 <= nums[i] <= 1000`

---

## Solution Explanation

We need to return an array that contains two copies of the input array `nums`.
To achieve this:

1. Initialize an empty list `ans`.
2. Loop twice since we want two copies of `nums`.
3. In each loop, append every element from `nums` to `ans`.
4. Finally, return `ans`.

This ensures that all elements from the first and second copies appear in the same order as in the original array.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  We iterate through the list twice, but since constants are ignored, the overall complexity remains `O(n)`.

- **Space Complexity:** `O(n)`
  A new list of size `2n` is created.

---

## Code Implementation

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
```

---
