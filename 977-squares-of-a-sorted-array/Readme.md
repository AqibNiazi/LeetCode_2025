# 977. Squares of a Sorted Array

## Problem

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

### Example 1

Input:
nums = [-4, -1, 0, 3, 10]

Output:
[0, 1, 9, 16, 100]

Explanation:
After squaring → [16, 1, 0, 9, 100]
After sorting → [0, 1, 9, 16, 100]

### Example 2

Input:
nums = [-7, -3, 2, 3, 11]

Output:
[4, 9, 9, 49, 121]

## Constraints

- 1 <= nums.length <= 10⁴
- -10⁴ <= nums[i] <= 10⁴
- nums is sorted in non-decreasing order

# Solution

## Intuition

Even though the array is sorted, squaring negative numbers can disturb the order.

For example:

nums = [-4, -1, 0, 3, 10]

After squaring:
[16, 1, 0, 9, 100]

The largest squared values come from numbers with the largest absolute values — which are located at both ends of the array.

So instead of squaring everything and sorting again, we can use a smarter approach to achieve O(n) time complexity.

## Approach 1: Brute Force (Square + Sort)

### Idea

1. Square every element in the array.
2. Sort the resulting array.
3. Return the sorted result.

### Why It Works

Since the input array is already sorted, squaring destroys the order due to negative values. Sorting again restores the correct order.

### Complexity

Time Complexity: O(n log n)

- O(n) to square elements
- O(n log n) to sort

Space Complexity: O(1) or O(n)

- Depends on sorting implementation

This approach is straightforward but does not satisfy the follow-up requirement.

## Approach 2: Optimal Two-Pointer Solution (O(n))

### Idea

Because the array is sorted:

- The largest absolute values are either at the beginning (large negative numbers) or at the end (large positive numbers).
- Their squares will be the largest values.

So we:

1. Use two pointers:
   - Left pointer at the beginning
   - Right pointer at the end

2. Compare absolute values
3. Insert the larger square into the result
4. Move the corresponding pointer inward
5. Since we insert larger values first, reverse the result at the end (or fill from back to front)

### Why It Works

We avoid sorting completely.
Each element is processed exactly once.

### Complexity

Time Complexity: O(n)

- Single pass using two pointers

Space Complexity: O(n)

- To store the result array

This satisfies the follow-up requirement of O(n) time.

## Key Takeaways

- Squaring a sorted array does not preserve sorted order because of negative numbers.
- The largest square always comes from either end of the array.
- Two-pointer technique is very useful when dealing with sorted arrays.
- This is a classic pattern problem for interviews.

## Final Recommendation

For interviews and production-level solutions, always prefer the Two-Pointer approach since it achieves:

- O(n) time
- Clean logic
- No additional sorting

This is the expected optimal solution for this problem.
