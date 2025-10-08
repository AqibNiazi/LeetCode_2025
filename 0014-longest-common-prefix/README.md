## 14. Longest Common Prefix

**Difficulty:** Easy  
**Topics:** String

---

### Problem Statement

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

---

### Example 1

**Input:**  
`strs = ["flower","flow","flight"]`

**Output:**  
`"fl"`

---

### Example 2

**Input:**  
`strs = ["dog","racecar","car"]`

**Output:**  
`""`

**Explanation:**  
There is no common prefix among the input strings.

---

### Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

---

### Solution

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
```

---

### Explanation

**Intuition:**
The longest common prefix must appear at the start of every string. So, we can compare characters at each position across all strings until a mismatch is found.

**Approach:**

1. Initialize an empty string `res` to store the common prefix.
2. Iterate through each character of the first string using its index.
3. For every index `i`, compare the character `strs[0][i]` with the same index character of all other strings.
4. If any string ends or has a different character, return the prefix collected so far.
5. If all strings match for that index, append the character to the prefix.
6. After the loop, return the result.

**Example Walkthrough:**
For `["flower", "flow", "flight"]`:

- Compare index 0 → `'f'` matches all.
- Compare index 1 → `'l'` matches all.
- Compare index 2 → mismatch (`'o'` vs `'i'`) → return `"fl"`.

---

### Complexity Analysis

- **Time Complexity:** O(N × M), where N is the number of strings and M is the length of the shortest string.
- **Space Complexity:** O(1), as only a few extra variables are used.

```

```
