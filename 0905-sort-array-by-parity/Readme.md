# 905. Sort Array By Parity

## Problem Description

Given an integer array `nums`, move all the **even integers** to the beginning of the array, followed by all the **odd integers**.

Return **any valid array** that satisfies this condition.

## Examples

### Example 1

**Input**

```id="e1"
nums = [3,1,2,4]
```

**Output**

```id="e2"
[2,4,3,1]
```

**Explanation**
Other valid outputs include: `[4,2,3,1]`, `[2,4,1,3]`, `[4,2,1,3]`

### Example 2

**Input**

```id="e3"
nums = [0]
```

**Output**

```id="e4"
[0]
```

## Constraints

- `1 <= nums.length <= 5000`
- `0 <= nums[i] <= 5000`

# Approach 1: Extra Arrays (Brute Force)

## Intuition

The simplest idea is:

- Separate numbers into **even** and **odd**
- Store them in different arrays
- Combine them at the end

👉 This is straightforward but uses extra space.

## Approach

1. Create two lists:
   - `even` → for even numbers
   - `odd` → for odd numbers

2. Traverse the array:
   - If number is even → add to `even`
   - Else → add to `odd`

3. Return `even + odd`

## Code

```python id="c1"
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        return even + odd
```

## Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
  - Extra arrays used

# Approach 2: Two Pointers (In-place Optimal)

## Intuition

Instead of using extra space:

👉 We can rearrange elements **in-place**

- Maintain a pointer `l` for position of next even number
- Traverse with pointer `r`
- Swap whenever we find an even number

## Approach

1. Initialize pointer `l = 0`
2. Traverse array using pointer `r`
3. If `nums[r]` is even:
   - Swap `nums[l]` and `nums[r]`
   - Increment `l`

4. Return modified array

## Code

```python id="c2"
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
```

## Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
  - In-place solution (optimal)

# Key Takeaways

- Brute force approach is simple but uses extra space
- Two-pointer approach is:
  - More efficient
  - In-place
  - Preferred in interviews

- This pattern is similar to:
  - Partitioning problems
  - QuickSort partition logic

# Final Verdict

| Approach     | Time | Space | Notes                        |
| ------------ | ---- | ----- | ---------------------------- |
| Extra Arrays | O(n) | O(n)  | Easy to understand           |
| Two Pointers | O(n) | O(1)  | Optimal & interview-friendly |
