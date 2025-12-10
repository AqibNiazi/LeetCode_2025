# 1. Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

---

### Example 1

**Input:**  
`nums = [2,7,11,15], target = 9`  
**Output:**  
`[0,1]`  
**Explanation:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

---

### Example 2

**Input:**  
`nums = [3,2,4], target = 6`  
**Output:**  
`[1,2]`

---

### Example 3

**Input:**  
`nums = [3,3], target = 6`  
**Output:**  
`[0,1]`

---

### Constraints

- `2 <= nums.length <= 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= target <= 10⁹`
- Only one valid answer exists.

---

### Follow-up

Can you come up with an algorithm that is less than `O(n²)` time complexity?

---

## Intuition

The brute-force approach would be to check every pair of numbers and see if they sum up to the target.  
However, this approach takes `O(n²)` time, which is inefficient for large input sizes.

To improve, we can use a **hash map (dictionary)** to store the numbers we’ve already seen and their indices.  
Then, for each number, we simply check if its complement (i.e., `target - num`) exists in the map.  
This allows us to find the pair in just one pass.

---

## Approach

1. Create an empty hash map `prevMap` to store previously visited numbers and their indices.
2. Iterate through the array using `enumerate()` to get both index `i` and value `n`.
3. For each element:
   - Compute the complement: `diff = target - n`
   - If `diff` exists in the hash map, return `[prevMap[diff], i]`
   - Otherwise, add the current number and its index to the hash map.
4. The problem guarantees exactly one valid solution, so we don’t need extra checks beyond the loop.

This approach ensures that we check each number only once, leading to linear time complexity.

---

## Complexity

- **Time Complexity:** `O(n)`  
  We traverse the list once, performing constant-time hash lookups and insertions.

- **Space Complexity:** `O(n)`  
  In the worst case, we store all numbers in the hash map.

---

## Code Implementation

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # value: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
```

---

## Example Walkthrough

**Input:**
`nums = [2,7,11,15], target = 9`

| Step | i   | n   | diff (target - n) | prevMap (before) | Action                   | Output |
| ---- | --- | --- | ----------------- | ---------------- | ------------------------ | ------ |
| 1    | 0   | 2   | 7                 | {}               | 7 not in map → add {2:0} | -      |
| 2    | 1   | 7   | 2                 | {2:0}            | 2 in map → return [0,1]  | [0,1]  |

**Result:** `[0,1]`

---

## Summary

By using a hash map to store previously seen numbers, we efficiently find the complement for each element in a single pass.
This converts the naive `O(n²)` search into an optimal `O(n)` solution using a clean and intuitive approach.
