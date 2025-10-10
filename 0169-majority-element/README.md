# 169. Majority Element

**Difficulty:** Easy  
**Topics:** Array, Divide and Conquer, Bit Manipulation

---

## Problem Statement

Given an array `nums` of size `n`, return the majority element.

The **majority element** is the element that appears more than ⌊n / 2⌋ times.  
You may assume that the majority element always exists in the array.

---

### Example 1

**Input:**  
`nums = [3,2,3]`  
**Output:**  
`3`

---

### Example 2

**Input:**  
`nums = [2,2,1,1,1,2,2]`  
**Output:**  
`2`

---

### Constraints

- `n == nums.length`
- `1 <= n <= 5 * 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`

---

### Follow-up

Could you solve the problem in **linear time** and in **O(1)** space?

---

## Solution Explanation

### Intuition

If one element appears more than half the time, even after pairing each occurrence of it with a different element, it will still remain unpaired in the end.  
This key insight leads to the **Boyer–Moore Voting Algorithm**, which efficiently identifies the majority element without extra memory.

---

### Approach

1. Initialize two variables:
   - `res` → stores the current candidate for majority.
   - `count` → keeps track of the balance between occurrences of `res` and other elements.
2. Iterate through each number in `nums`:
   - If `count` is 0, set the current number as the new candidate (`res = num`).
   - If the current number equals the candidate, increment `count`; otherwise, decrement it.
3. After one pass, `res` holds the majority element.

---

### Complexity Analysis

- **Time Complexity:** `O(n)`  
  We iterate through the array once.
- **Space Complexity:** `O(1)`  
  Only a few variables are used; no additional data structures.

---

### Code Implementation

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res
```

---

### Example Walkthrough

**Input:**
`nums = [2,2,1,1,1,2,2]`

| Step | num | count before | res before | Action           | count after | res after |
| ---- | --- | ------------ | ---------- | ---------------- | ----------- | --------- |
| 1    | 2   | 0            | 0          | count==0 → res=2 | 1           | 2         |
| 2    | 2   | 1            | 2          | num==res → +1    | 2           | 2         |
| 3    | 1   | 2            | 2          | num!=res → -1    | 1           | 2         |
| 4    | 1   | 1            | 2          | num!=res → -1    | 0           | 2         |
| 5    | 1   | 0            | 2          | count==0 → res=1 | 1           | 1         |
| 6    | 2   | 1            | 1          | num!=res → -1    | 0           | 1         |
| 7    | 2   | 0            | 1          | count==0 → res=2 | 1           | 2         |

**Final Output:** `2`

---

### Summary

The Boyer–Moore Voting Algorithm provides an optimal solution for identifying the majority element in linear time and constant space.
It leverages the fact that the majority element’s frequency exceeds the sum of all others, ensuring it remains as the final candidate after all cancellations.
