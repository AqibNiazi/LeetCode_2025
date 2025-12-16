# 1470. Shuffle the Array

## Problem Statement

You are given an array `nums` consisting of `2n` elements arranged as:

```

[x1, x2, ..., xn, y1, y2, ..., yn]

```

Your task is to return the array rearranged as:

```

[x1, y1, x2, y2, ..., xn, yn]

```

---

## Examples

**Example 1**

```

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]

```

**Example 2**

```

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

```

**Example 3**

```

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]

```

## Constraints

- `1 <= n <= 500`
- `nums.length == 2n`
- `1 <= nums[i] <= 1000`

## Solution 1: Using an Extra Array

### Intuition

The array is already split into two halves:

- First half contains all `x` values
- Second half contains all `y` values

We can iterate through the first `n` elements and alternately append values from both halves into a new array.

### Approach

1. Create an empty result array.
2. Loop from `0` to `n - 1`.
3. Append `nums[i]` and `nums[i + n]` in each iteration.
4. Return the result array.

### Code

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result
```

### Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Solution 2: Using Bit Manipulation (In-place)

### Intuition

Since the constraints guarantee that each number fits within 10 bits (`nums[i] <= 1000`), we can store two numbers in a single integer using bit manipulation.

This allows us to rearrange the array **in-place** without using extra space.

### Approach

1. For each index `i` in the first half:

   - Left shift `nums[i]` by 10 bits.
   - Use bitwise OR to store `nums[i + n]` in the lower bits.

2. Traverse backward and extract:

   - `x` using right shift
   - `y` using bit masking

3. Place `x` and `y` in correct positions.

### Code

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i + n]

        j = 2 * n - 1
        for i in range(n - 1, -1, -1):
            y = nums[i] & (2**10 - 1)
            x = nums[i] >> 10
            nums[j] = y
            nums[j - 1] = x
            j -= 2

        return nums
```

### Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

## Notes

- Solution 1 is straightforward and easy to understand.
- Solution 2 is more advanced and useful when in-place modification is required.
- Both solutions satisfy the problem constraints efficiently.
