# 167. Two Sum II - Input Array Is Sorted

## Problem Description

Given a **1-indexed array** of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number.

Return the indices of the two numbers as an integer array `[index1, index2]` of length 2, where `1 <= index1 < index2 <= numbers.length`.

You may not use the same element twice, and your solution must use **only constant extra space**.

---

### Example 1

**Input:**
`numbers = [2,7,11,15], target = 9`
**Output:**
`[1,2]`
**Explanation:**
The sum of 2 and 7 is 9. Therefore, index1 = 1 and index2 = 2.

---

### Example 2

**Input:**
`numbers = [2,3,4], target = 6`
**Output:**
`[1,3]`
**Explanation:**
The sum of 2 and 4 is 6. Therefore, index1 = 1 and index2 = 3.

---

### Example 3

**Input:**
`numbers = [-1,0], target = -1`
**Output:**
`[1,2]`
**Explanation:**
The sum of -1 and 0 is -1. Therefore, index1 = 1 and index2 = 2.

---

### Constraints

- `2 <= numbers.length <= 3 * 10⁴`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- `-1000 <= target <= 1000`
- The tests are generated such that there is **exactly one solution**.

---

## Intuition

Since the input array is already sorted, we can efficiently find the two numbers using the **two-pointer technique** instead of a brute-force approach.
By starting from both ends of the array, we can adjust our pointers based on whether the current sum is less than or greater than the target.

---

## Approach

1. Initialize two pointers:

   - `l` at the start (`0`)
   - `r` at the end (`len(numbers) - 1`)

2. Compute the sum of the two numbers: `currSum = numbers[l] + numbers[r]`.
3. If `currSum` is greater than the target, move the right pointer left (`r -= 1`) to reduce the sum.
4. If `currSum` is less than the target, move the left pointer right (`l += 1`) to increase the sum.
5. If `currSum` equals the target, return `[l + 1, r + 1]` (adjusted for 1-indexing).

This approach ensures that each element is checked at most once, resulting in an efficient linear-time solution.

---

## Code Implementation

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)` — Each element is visited at most once.
- **Space Complexity:** `O(1)` — No additional data structures are used beyond constant variables.

---

## Key Takeaways

- Leverages the **sorted property** of the array to avoid nested loops.
- Uses **two pointers** to achieve optimal efficiency.
- Simple, readable, and optimal for the given constraints.
