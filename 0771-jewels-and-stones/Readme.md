# 771. Jewels and Stones

## Problem

You are given two strings:

- `jewels`: represents the types of stones that are jewels
- `stones`: represents the stones you have

Each character in `stones` is a stone you own. You need to count how many of those stones are also jewels.

Notes:

- Letters are case-sensitive (`"a"` is different from `"A"`).
- All characters in `jewels` are unique.

---

### Example 1

**Input**

```

jewels = "aA", stones = "aAAbbbb"

```

**Output**

```

3

```

### Example 2

**Input**

```

jewels = "z", stones = "ZZ"

```

**Output**

```

0

```

### Intuition

For every stone we have, we need to check whether it belongs to the set of jewels.
A direct comparison works, but it can be slow if we repeatedly scan the `jewels` string.
Using a set allows faster lookups.

## Approach

### Solution 1: Direct Comparison

- Iterate through each character in `stones`.
- Check if it exists in the `jewels` string.
- Increment the count when it does.

### Solution 2: Using a Set (Optimized)

- Convert `jewels` into a set for O(1) lookups.
- Iterate through `stones` and count characters that exist in the set.

## Solution Code

### Solution 1: Brute Force

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_count = 0
        for ch in stones:
            if ch in jewels:
                jewels_count += 1
        return jewels_count
```

### Solution 2: Using a Set

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        jewels_count = 0
        for ch in stones:
            if ch in jewels_set:
                jewels_count += 1
        return jewels_count
```

## Complexity Analysis

### Solution 1

- **Time Complexity:** O(n × m)

  - `n` = length of `stones`
  - `m` = length of `jewels`

- **Space Complexity:** O(1)

### Solution 2

- **Time Complexity:** O(n + m)
- **Space Complexity:** O(m)

## Key Takeaway

Using a set is the cleanest and most efficient way to solve this problem since it reduces repeated lookup time and keeps the code simple.
