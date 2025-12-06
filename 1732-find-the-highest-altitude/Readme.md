# 1732. Find the Highest Altitude

## Problem

A biker is going on a road trip consisting of `n + 1` points.
The biker starts at point `0` with an altitude of `0`.

You are given an integer array `gain` of length `n`, where:

`gain[i]` = net gain in altitude from point `i` to point `i + 1`.

Return the highest altitude the biker reaches at any point during the trip.

### Example 1

Input: `gain = [-5,1,5,0,-7]`
Output: `1`
Explanation:
Altitudes = `[0, -5, -4, 1, 1, -6]`
Highest altitude = `1`.

### Example 2

Input: `gain = [-4,-3,-2,-1,4,3,2]`
Output: `0`
Explanation:
Altitudes = `[0, -4, -7, -9, -10, -6, -3, -1]`
Highest altitude = `0`.

### Constraints

- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`

---

## Intuition

The biker starts at altitude 0. Each value in the `gain` array represents the change in altitude from one point to the next.
By accumulating these changes step by step, we can track the altitude at each point.
The highest altitude is simply the maximum value reached during this cumulative process.

---

## Approach

1. Initialize `alt = 0` to represent the current altitude.
2. Initialize `max_alt = 0` because the biker starts at altitude 0.
3. Loop through each value in `gain`:

   - Add the current gain value to `alt` to update the altitude.
   - Update `max_alt` if the new altitude is higher.

4. Return `max_alt` at the end.

The altitudes are not stored in an array; instead, we compute them on the fly for efficiency.

---

## Complexity

**Time Complexity:**
O(n), because we traverse the list once.

**Space Complexity:**
O(1), since we do not use any extra data structures and only track two variables.

---

## Code

```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        max_alt = 0

        for change in gain:
            alt += change
            max_alt = max(max_alt, alt)
        return max_alt
```

---
