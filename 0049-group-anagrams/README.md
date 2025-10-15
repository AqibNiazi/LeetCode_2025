# 49. Group Anagrams

## Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### Example 1

**Input:**

```
strs = ["eat","tea","tan","ate","nat","bat"]
```

**Output:**

```
[["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Explanation:**

- There is no string in `strs` that can be rearranged to form `"bat"`.
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

---

### Example 2

**Input:**

```
strs = [""]
```

**Output:**

```
[[""]]
```

---

### Example 3

**Input:**

```
strs = ["a"]
```

**Output:**

```
[["a"]]
```

---

### Constraints

- 1 <= strs.length <= 10⁴
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

---

## Intuition

Anagrams are words that have the same characters with the same frequency, but possibly in a different order.
If two words share the same character frequency pattern (for all letters from `'a'` to `'z'`), they belong to the same group of anagrams.
We can use this property to group anagrams efficiently using a hash map.

---

## Approach

1. Create a hash map (`defaultdict(list)`) where:

   - **Key:** A tuple representing the frequency of each character (`a` to `z`).
   - **Value:** List of words that match that frequency pattern.

2. For each string in `strs`:

   - Initialize a frequency list of size 26 with all zeros.
   - Increment the count for each character.
   - Convert the frequency list into a tuple (so it can be used as a dictionary key).
   - Append the word to the corresponding key in the hash map.

3. Return all the grouped lists from the hash map as the final result.

---

## Code Implementation

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Mapping character frequency to list of anagrams

        for s in strs:
            count = [0] * 26  # Represents letters 'a' to 'z'
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())
```

---

## Complexity Analysis

- **Time Complexity:** O(N \* K)

  - N = number of strings
  - K = average length of each string
    For each string, we count characters in O(K) time.

- **Space Complexity:** O(N \* K)

  - Due to storing the character frequency keys and the grouped anagrams in the hash map.
