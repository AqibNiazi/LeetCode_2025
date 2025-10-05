## 💡 Intuition

When checking if a string is a palindrome, we compare characters from both ends toward the center.
If all characters match, it’s a palindrome.
However, if we find a mismatch, we have one chance to **skip either the left or right character** and check if the rest forms a palindrome.

---

## 🚀 Approach

1. Use two pointers:

   - `l` (left) starting at index `0`.
   - `r` (right) starting at index `len(s) - 1`.

2. Compare characters while `l < r`.
3. If `s[l] != s[r]`, try two possibilities:

   - Skip the left character → `s[l+1:r+1]`
   - Skip the right character → `s[l:r]`

4. If either substring is a palindrome, return `True`.
5. If the loop finishes without mismatches, the string is already a palindrome.

---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n)` — Each character is compared at most once.
- **Space Complexity:** `O(1)` — Constant space used for pointers.

---

## 🧠 Code Implementation

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l, r = l + 1, r - 1
        return True
```

---

## 🧩 Example Walkthrough

### Example: `s = "abca"`

| Step | l   | r   | s[l] | s[r] | Action                                            |
| ---- | --- | --- | ---- | ---- | ------------------------------------------------- |
| 1    | 0   | 3   | 'a'  | 'a'  | Match → move inward                               |
| 2    | 1   | 2   | 'b'  | 'c'  | Mismatch → try skipping                           |
|      |     |     |      |      | Check `"ca"` and `"ab"`                           |
|      |     |     |      |      | `"ab"` reversed = `"ba"` → ❌                     |
|      |     |     |      |      | `"ca"` reversed = `"ac"` → ❌                     |
|      |     |     |      |      | Wait — actually skipping `'c'` makes `"aba"` → ✅ |

Hence the result is `True`.

---

## 🧾 Summary

✅ Uses **two-pointer** technique
✅ Checks **both skip options** efficiently
✅ Works in **O(n)** time
✅ Handles strings up to `10⁵` length
