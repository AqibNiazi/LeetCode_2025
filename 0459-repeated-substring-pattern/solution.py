class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)  # first calculate length of the string

        # Then we iterate a string
        # A repeating substring cannot be longer than half the string
        for l in range(n//2, 0 , -1):
            # we check either l completly divides n
            if n % l == 0:
                # Calculate repetition count
                times = n // l
                #Extract candidate substring
                pattern = s[:l]
                # Build repeated string
                new_str = ""

                while times > 0:
                    new_str += pattern
                    if new_str == s:
                        return True
                    times -= 1
        return False





  
