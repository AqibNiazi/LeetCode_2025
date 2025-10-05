# 🧩 Problem — Valid Palindrome II

You are given a string `s`. Return `true` if `s` can be a palindrome **after deleting at most one character** from it.

A **palindrome** is a string that reads the same forward and backward.

> **Note:** Alphanumeric characters consist of letters (`A–Z`, `a–z`) and numbers (`0–9`).

---

## ✨ Example 1

**Input:**

```text
s = "aca"
```

**Output:**

```text
true
```

**Explanation:**
`"aca"` is already a palindrome.

---

## ✨ Example 2

**Input:**

```text
s = "abbadc"
```

**Output:**

```text
false
```

**Explanation:**
`"abbadc"` is not a palindrome and cannot be made one by deleting just a single character.

---

## ✨ Example 3

**Input:**

```text
s = "abbda"
```

**Output:**

```text
true
```

**Explanation:**
We can delete the character `'d'` to make `"abba"`, which is a palindrome.

---

## 🔒 Constraints

- `1 <= s.length <= 100,000`
- `s` consists only of lowercase English letters (`a–z`).

---
