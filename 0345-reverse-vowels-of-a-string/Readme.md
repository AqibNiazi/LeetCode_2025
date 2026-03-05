# 345. Reverse Vowels of a String

## Problem

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `a`, `e`, `i`, `o`, and `u`.
They may appear in both lowercase and uppercase and can appear multiple times.

## Example 1

Input:
s = "IceCreAm"

Output:
"AceCreIm"

Explanation:
The vowels are `['I', 'e', 'e', 'A']`.
After reversing them → `['A', 'e', 'e', 'I']`.

## Example 2

Input:
s = "leetcode"

Output:
"leotcede"

## Constraints

1 <= s.length <= 3 \* 10⁵
s consists of printable ASCII characters

# Solution

## Intuition

We only need to reverse the vowels, not the entire string.

If we scan from both ends of the string:

• Move the left pointer forward until we find a vowel
• Move the right pointer backward until we find a vowel
• Swap them
• Continue until the pointers meet

This ensures vowels are reversed while consonants remain in place.

## Approach

1. Store all vowels in a set for O(1) lookup.
2. Convert the string into a list because strings are immutable.
3. Use two pointers:
   - `left` starting from index 0
   - `right` starting from the last index

4. Move pointers inward until vowels are found.
5. Swap the vowels.
6. Join the list back into a string.

## Code

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)
```

## Complexity Analysis

Time Complexity: O(n)
Each character is visited at most once.

Space Complexity: O(n)
We convert the string into a list.

## Key Takeaway

This is a classic two-pointer problem.
Whenever you need to reverse specific elements in a string or array while preserving others, two pointers moving inward is often the optimal approach.
