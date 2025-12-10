# Stack Solution

# Time Complexity: O(n+m)
# Space Complexity: O(n+m)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string:str) -> List[str]:
            stack = []
            for ch in string:
                if ch == "#":
                    if stack:
                        stack.pop()
                    # skip else
                else:
                    stack.append(ch)
            return stack
        return build(s) == build(t)

# Two Pointer Solution
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            # find next valid char in s
            skip = 0
            while i >= 0:
                if s[i] == '#':
                    skip += 1
                    i -= 1
                elif skip > 0:
                    skip -= 1
                    i -= 1
                else:
                    break  # s[i] is a valid character
            # find next valid char in t
            skip = 0
            while j >= 0:
                if t[j] == '#':
                    skip += 1
                    j -= 1
                elif skip > 0:
                    skip -= 1
                    j -= 1
                else:
                    break  # t[j] is a valid character

            # Compare current characters (if any)
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                # One has a char remaining while the other doesn't
                return False

            i -= 1
            j -= 1

        return True

  
        
    

        