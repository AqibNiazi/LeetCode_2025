# 1832. Check if the Sentence Is Pangram

## 📝 Problem

A **pangram** is a sentence where every letter of the English alphabet appears at least once.

Given a string `sentence` containing only lowercase English letters, return `true` if `sentence` is a pangram, or `false` otherwise.

### 📌 Example 1:

```

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true

```

### 📌 Example 2:

```

Input: sentence = "leetcode"
Output: false

```

### 🔒 Constraints:

- `1 <= sentence.length <= 1000`
- `sentence` consists of lowercase English letters.

# 🚀 Solutions

# 1️⃣ Brute Force Solution

## 💡 Intuition

To check if a sentence is a pangram, we must ensure that **all 26 lowercase English letters** are present.

A straightforward approach is:

- Iterate through each character from `'a'` to `'z'`
- Check if it exists in the given string

If any character is missing → return `False`

## ⚙️ Approach

1. Loop through all characters from `'a'` to `'z'`
2. For each character:
   - Check if it is present in the string
3. If any character is not found → return `False`
4. If all characters are found → return `True`

## ⏱ Complexity

- **Time Complexity:** `O(26 * n) ≈ O(n)`
- **Space Complexity:** `O(1)`

## 💻 Code

```python
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch not in sentence:
                return False
        return True
```

# 2️⃣ Better Approach — Using Set

## 💡 Intuition

A **set** only stores unique elements.

So if the sentence is a pangram:

- It must contain **all 26 unique characters**

## ⚙️ Approach

1. Convert the string into a set
2. Count unique characters
3. If size of set is `26` → return `True`
4. Otherwise → return `False`

## ⏱ Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(26) ≈ O(1)`

## 💻 Code

```python
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
```
