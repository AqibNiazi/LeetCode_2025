# 2215. Find the Difference of Two Arrays

## Problem Statement

Given two 0-indexed integer arrays `nums1` and `nums2`, return a list `answer` of size 2 where:

- `answer[0]` contains all **distinct integers** in `nums1` that are **not present** in `nums2`.
- `answer[1]` contains all **distinct integers** in `nums2` that are **not present** in `nums1`.

The integers in the result lists can be returned in **any order**.

---

## Examples

**Example 1**

```

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

```

**Example 2**

```

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]

```

---

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `-1000 <= nums1[i], nums2[i] <= 1000`

---

## Intuition

To efficiently check whether an element exists in the other array, we need **fast lookups**.  
Using a set allows membership checks in `O(1)` time.

By converting both arrays into sets:

- We can quickly identify elements that exist in one array but not the other.
- Sets also automatically handle duplicates, ensuring the result contains only distinct values.

---

## Approach

1. Convert `nums1` and `nums2` into sets (`nums1Set` and `nums2Set`).
2. Traverse `nums1` and collect elements that are **not** in `nums2Set`.
3. Traverse `nums2` and collect elements that are **not** in `nums1Set`.
4. Convert the result sets into lists and return them as a list of two lists.

---

## Solution (Python)

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set, nums2Set = set(nums1), set(nums2)
        res1, res2 = set(), set()

        for n in nums1:
            if n not in nums2Set:
                res1.add(n)

        for n in nums2:
            if n not in nums1Set:
                res2.add(n)

        return [list(res1), list(res2)]
```

---

## Complexity Analysis

- **Time Complexity:** `O(n + m)`
  where `n` is the length of `nums1` and `m` is the length of `nums2`.

- **Space Complexity:** `O(n + m)`
  due to the use of sets for storing unique elements.

---

## Key Takeaway

- Sets are ideal when you need **uniqueness** and **fast lookups**.
- Converting arrays to sets simplifies logic and improves performance for comparison-based problems.
