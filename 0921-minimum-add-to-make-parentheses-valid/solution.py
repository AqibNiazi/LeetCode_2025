class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0   # number of unmatched open "("
        res = 0        # number of insertions needed so far
        for c in s:
            if c == "(":
                open_cnt += 1
            else:   # c == ")"
                open_cnt -= 1
                if open_cnt < 0:
                  # we have an extra ')', need to insert '('
                    res += 1
                    open_cnt = 0

        # remaining open_cnt '(' need ')' to match them    
        return res + open_cnt
        
        # Time: O(n)
        # Space: O(1)