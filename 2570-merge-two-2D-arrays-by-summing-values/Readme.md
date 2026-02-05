# 2570. Merge Two 2D Arrays by Summing Values

## Problem

You are given two 2D integer arrays `nums1` and `nums2`.

- `nums1[i] = [id_i, val_i]` means the number with id `id_i` has value `val_i`.
- `nums2[i] = [id_i, val_i]` means the number with id `id_i` has value `val_i`.

Each array:

- Contains **unique ids**
- Is sorted in **ascending order by id**

### Goal

Merge the two arrays into one array that:

- Is sorted in ascending order by id
- Contains each id **only once**
- Stores the **sum of values** for matching ids
- Includes ids that appear in **either** array

---

## Examples

### Example 1

```

Input:
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]

Output:
[[1,6],[2,3],[3,2],[4,6]]

```

### Example 2

```

Input:
nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]

Output:
[[1,3],[2,4],[3,6],[4,3],[5,5]]

```

---

## Constraints

- `1 <= nums1.length, nums2.length <= 200`
- `nums1[i].length == nums2[j].length == 2`
- `1 <= id_i, val_i <= 1000`
- Both arrays are sorted in strictly ascending order by id

---

## Solution

### Intuition

Since both arrays are already sorted by id, this problem is very similar to merging two sorted arrays.  
Using two pointers allows us to compare ids efficiently and build the result in sorted order.

---

### Approach

1. Initialize two pointers `i` and `j` for `nums1` and `nums2`.
2. Compare the current ids:
   - If `nums1[i][0] < nums2[j][0]`, add `nums1[i]` to the result.
   - If `nums1[i][0] > nums2[j][0]`, add `nums2[j]` to the result.
   - If ids are equal, add a new pair with the summed values.
3. Move the corresponding pointer(s).
4. Append any remaining elements from either array.
5. Return the merged result.

---

### Code

```python
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] < nums2[j][0]:
                result.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                result.append(nums2[j])
                j += 1
            else:
                result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1

        while i < len(nums1):
            result.append(nums1[i])
            i += 1

        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        return result
```

---

### Complexity

- **Time Complexity:** `O(n + m)`
  where `n = len(nums1)` and `m = len(nums2)`
- **Space Complexity:** `O(n + m)`
  for storing the merged result

---

## Key Takeaway

This problem is a classic **two-pointer merge** pattern. When arrays are sorted, using two pointers leads to an optimal and clean solution without extra data structures.
