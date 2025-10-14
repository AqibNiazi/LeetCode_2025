# 88. Merge Sorted Array

**Difficulty:** Easy
**Topics:** Array, Two Pointers, Sorting

---

## Question

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`.
To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored.
`nums2` has a length of `n`.

---

### Example 1

**Input:**

```
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
```

**Output:**

```
[1,2,2,3,5,6]
```

**Explanation:**
The arrays we are merging are `[1,2,3]` and `[2,5,6]`.
The result of the merge is `[1,2,2,3,5,6]` with the underlined elements coming from `nums1`.

---

### Example 2

**Input:**

```
nums1 = [1], m = 1
nums2 = [], n = 0
```

**Output:**

```
[1]
```

---

### Example 3

**Input:**

```
nums1 = [0], m = 0
nums2 = [1], n = 1
```

**Output:**

```
[1]
```

**Explanation:**
Because `m = 0`, there are no elements in `nums1`. The 0 is only there to ensure the merge result can fit in `nums1`.

---

### Constraints

```
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9
```

**Follow up:**
Can you come up with an algorithm that runs in `O(m + n)` time?

---

## Solution

### Intuition

Since both arrays are already sorted, we can efficiently merge them without sorting again.
The main idea is to fill `nums1` from the **end**, where extra space is already available, to avoid overwriting any existing elements before comparing.

---

### Approach

1. Use three pointers:

   - `i = m - 1` → last valid element in `nums1`
   - `j = n - 1` → last element in `nums2`
   - `last = m + n - 1` → last position in `nums1`

2. Iterate while `j >= 0`:

   - Compare `nums1[i]` and `nums2[j]`.
   - Place the larger element at `nums1[last]`.
   - Move the corresponding pointer backward.

3. If there are remaining elements in `nums2`, copy them into `nums1`.

This approach ensures all elements are merged in sorted order **in-place**.

---

### Code Implementation

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        i, j = m - 1, n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1
```

---

### Complexity Analysis

- **Time Complexity:** `O(m + n)` — each element is processed once.
- **Space Complexity:** `O(1)` — merging is done in-place without extra space.
