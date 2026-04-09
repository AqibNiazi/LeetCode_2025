# 496. Next Greater Element I

## Problem Description

The **next greater element** of some element `x` in an array is the first element that is **greater than `x` and appears to the right of `x`** in the same array.

You are given two **distinct** integer arrays `nums1` and `nums2`, where:

* `nums1` is a subset of `nums2`
* All elements are unique

For each element in `nums1`, find its next greater element in `nums2`.
If no such element exists, return `-1` for that position.


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



## Constraints

* `1 <= nums1.length <= nums2.length <= 1000`
* `0 <= nums1[i], nums2[i] <= 10^4`
* All integers are unique
* All elements of `nums1` appear in `nums2`



# 🧠 Brute Force Solution

## Intuition

The most straightforward idea is:

* For each element in `nums1`, locate it in `nums2`
* Then scan all elements **to the right** in `nums2`
* The first greater element found is the answer
* If none exists → return `-1`

This directly follows the problem definition but is inefficient due to repeated scanning.


## Approach

1. Create a hashmap to store indices of elements in `nums1`
2. Initialize result array with `-1`
3. Traverse `nums2`:

   * If current element exists in `nums1`, start checking its right side
   * Find the first greater element and update result
4. Return result array


## Brute Force Code

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n: i for i, n in enumerate(nums1)}
        result = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue

            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    result[idx] = nums2[j]
                    break

        return result
```


## Complexity Analysis (Brute Force)

* **Time Complexity:** `O(n * m)`

  * For each element, we may scan the rest of the array
* **Space Complexity:** `O(n)`

  * Hashmap + result array


# ⚡ Efficient Solution (Monotonic Stack)

## Intuition

Brute force wastes time by repeatedly scanning.

To optimize:

* We compute next greater elements in **one pass**
* Use a **monotonic decreasing stack**
* Store only elements from `nums1` that we care about
* When a greater element appears, resolve pending elements


## Approach

1. Store indices of `nums1` in hashmap
2. Initialize result array with `-1`
3. Use a stack to track unresolved elements
4. Traverse `nums2`:

   * While stack not empty and current > stack top:

     * Pop and update result
   * If current element is in `nums1`, push to stack
5. Return result


## Efficient Solution Code

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


## Complexity Analysis (Efficient)

* **Time Complexity:** `O(n + m)`

  * Each element is processed once
* **Space Complexity:** `O(n)`

  * Stack + hashmap


## 🚀 Key Takeaways

* Brute force is simple but inefficient (`O(n*m)`)
* Monotonic stack reduces complexity to **linear time**
* Very common pattern for:

  * Next Greater Element
  * Next Smaller Element
  * Stock Span problems


