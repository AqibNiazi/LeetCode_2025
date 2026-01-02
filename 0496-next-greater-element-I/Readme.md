# 496. Next Greater Element I

## Problem Description

The **next greater element** of some element `x` in an array is the first element that is **greater than `x` and appears to the right of `x`** in the same array.

You are given two **distinct** integer arrays `nums1` and `nums2`, where:

- `nums1` is a subset of `nums2`
- All elements are unique

For each element in `nums1`, find its next greater element in `nums2`.
If no such element exists, return `-1` for that position.

---

## Examples

### Example 1

**Input**

```

nums1 = [4,1,2]
nums2 = [1,3,4,2]

```

**Output**

```

[-1,3,-1]

```

### Example 2

**Input**

```

nums1 = [2,4]
nums2 = [1,2,3,4]

```

**Output**

```

[3,-1]

```

---

## Constraints

- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 10^4`
- All integers in `nums1` and `nums2` are unique
- All elements of `nums1` appear in `nums2`

---

## Intuition

A brute-force solution would check, for every element in `nums1`, all elements to the right in `nums2`. This would be inefficient.

To optimize:

- We want to **precompute the next greater element** for elements in `nums2`
- A **monotonic decreasing stack** helps track elements waiting for a greater value
- Since we only care about elements in `nums1`, we store their indices for quick lookup

---

## Approach

1. Create a hashmap to store the index of each value in `nums1`
2. Initialize a result array with `-1` for all elements
3. Use a stack to keep track of elements from `nums2` whose next greater element is not yet found
4. Traverse `nums2`:
   - While the stack is not empty and the current number is greater than the top of the stack:
     - Pop from the stack and update its next greater value in the result
   - If the current number exists in `nums1`, push it onto the stack
5. Return the result array

---

## Solution Code

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for curr in nums2:
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = curr
            if curr in nums1Idx:
                stack.append(curr)

        return res
```

---

## Complexity Analysis

- **Time Complexity:** `O(n + m)`

  - `n = len(nums1)`
  - `m = len(nums2)`
  - Each element is pushed and popped from the stack at most once

- **Space Complexity:** `O(n)`

  - Hashmap for `nums1` indices
  - Stack for tracking elements

---

## Key Takeaways

- Monotonic stacks are very effective for **next greater / smaller element** problems
- Hashmaps help reduce lookup time from `O(n)` to `O(1)`
- This approach efficiently satisfies the follow-up requirement
