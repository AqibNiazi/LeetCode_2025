# 1512. Number of Good Pairs

## Problem Statement

Given an array of integers `nums`, return the number of **good pairs**.

A pair `(i, j)` is called **good** if:

- `nums[i] == nums[j]`
- `i < j`

---

## Examples

### Example 1

```

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: The good pairs are (0,3), (0,4), (3,4), (2,5).

```

### Example 2

```

Input: nums = [1,1,1,1]
Output: 6

```

### Example 3

```

Input: nums = [1,2,3]
Output: 0

```

---

## Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

---

## Intuition

For every number in the array, a good pair is formed with all **previous occurrences** of the same number.  
So instead of checking all pairs, we can keep track of how many times we have already seen a number.

Each time we see a number again, it forms as many new good pairs as its current frequency.

---

## Approach

1. Use a hash map (`count`) to store the frequency of each number.
2. Traverse the array from left to right.
3. For each number:
   - If it already exists in the map, add its current frequency to the answer.
   - Increment its frequency.
4. Return the total count of good pairs.

---

## Solution (Python)

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        good_pairs = 0

        for num in nums:
            if num in count:
                good_pairs += count[num]
                count[num] += 1
            else:
                count[num] = 1

        return good_pairs
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  Each element is processed once.

- **Space Complexity:** `O(n)`
  Extra space is used for the hash map to store frequencies.

---
