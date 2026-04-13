# 268. Missing Number

## Problem

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.


## Examples

**Example 1**

```

Input: nums = [3,0,1]
Output: 2

```

**Example 2**

```

Input: nums = [0,1]
Output: 2

```

**Example 3**

```

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

```


## Constraints

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All values in `nums` are unique


## Solution 1: Using Set

### Intuition

Since all numbers are in the range `[0, n]`, we can store all values in a set and check which number in this range is missing.

### Approach

1. Convert the array into a set.
2. Iterate from `0` to `n`.
3. Return the first number that does not exist in the set.

### Code

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
```

### Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`


## Solution 2: Using Sum Formula

### Intuition

The sum of numbers from `0` to `n` is known using the formula:

```
n * (n + 1) / 2
```

The missing number is the difference between the expected sum and the actual sum of the array.

### Approach

1. Compute the expected sum using the formula.
2. Compute the actual sum of the array.
3. Return the difference.

### Code

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
```

### Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`


## Solution 3: Using XOR

### Intuition

XOR has useful properties:

- `a ^ a = 0`
- `a ^ 0 = a`

If we XOR all numbers from `0` to `n` and also XOR all numbers in the array, all matching values cancel out, leaving only the missing number.

### Approach

1. XOR all values from `0` to `n`.
2. XOR all values in the array.
3. The final XOR result is the missing number.

### Code

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)

        for i in range(n + 1):
            xor ^= i

        for num in nums:
            xor ^= num

        return xor
```

### Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`


## Summary

- **Set solution** is easy to understand but uses extra space.
- **Sum formula** is simple and optimal in space.
- **XOR approach** is the most elegant and avoids overflow issues.

Both **Sum** and **XOR** solutions satisfy the follow-up requirement of `O(n)` time and `O(1)` extra space.
