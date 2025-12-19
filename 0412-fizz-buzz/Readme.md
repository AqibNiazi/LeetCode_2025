# 412. Fizz Buzz

**Difficulty:** Easy  
**Topics:** Math, Simulation

---

## Problem Statement

Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by both 3 and 5.
- `answer[i] == "Fizz"` if `i` is divisible by 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == i` (as a string) if none of the above conditions are true.

---

## Examples

### Example 1

**Input:**  
`n = 3`

**Output:**  
`["1", "2", "Fizz"]`

### Example 2

**Input:**  
`n = 5`

**Output:**  
`["1", "2", "Fizz", "4", "Buzz"]`

### Example 3

**Input:**  
`n = 15`

**Output:**  
`["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]`

## Intuition

For each number from `1` to `n`, we need to decide what string to add based on divisibility rules.  
Checking divisibility by `3` and `5` allows us to determine whether to append `"Fizz"`, `"Buzz"`, `"FizzBuzz"`, or the number itself.

## Approach

1. Initialize an empty list `result`.
2. Loop from `1` to `n`.
3. For each number:
   - If it is divisible by `3`, start with `"Fizz"`.
   - If it is also divisible by `5`, append `"Buzz"` to it.
   - If it is only divisible by `5`, use `"Buzz"`.
   - Otherwise, convert the number to a string.
4. Append the result for each number to the list.
5. Return the final list.

---

## Solution (Python)

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0:
                ans = "Fizz"
                if i % 5 == 0:
                    ans += "Buzz"
            elif i % 5 == 0:
                ans = "Buzz"
            else:
                ans = str(i)
            result.append(ans)

        return result
```

## Complexity Analysis

- **Time Complexity:** `O(n)`
  We iterate through the numbers from `1` to `n` once.

- **Space Complexity:** `O(n)`
  The output list stores `n` strings.

## Notes

- This is a classic problem to practice conditional logic and clean code structure.
- Handling the `FizzBuzz` case first avoids duplicate checks.
