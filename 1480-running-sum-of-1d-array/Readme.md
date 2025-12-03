# 1480. Running Sum of 1d Array

## Problem

Given an array `nums`, the running sum of the array is defined as:

`runningSum[i] = nums[0] + nums[1] + ... + nums[i]`

Return the running sum of `nums`.

### Example 1

Input: `nums = [1,2,3,4]`
Output: `[1,3,6,10]`
Explanation: Running sum is `[1, 1+2, 1+2+3, 1+2+3+4]`.

### Example 2

Input: `nums = [1,1,1,1,1]`
Output: `[1,2,3,4,5]`

### Example 3

Input: `nums = [3,1,2,10,1]`
Output: `[3,4,6,16,17]`

### Constraints

- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`

---

## Intuition

To compute the running sum, each element should represent the total sum of all elements before it including itself. Instead of recalculating the sum every time, we can build the result progressively by adding the previous running total to the current number.

---

## Approach

Start from index `1` because index `0` is already its own running sum.
For every index `i`, update `nums[i]` by adding the value of `nums[i - 1]`, which now holds the running sum up to the previous position.
Continue until the end of the array and return the updated list.

---

## Complexity

**Time Complexity:**
O(n), because we traverse the array once.

**Space Complexity:**
O(1), because we update the array in-place without using extra space.

---

## Code

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
```
