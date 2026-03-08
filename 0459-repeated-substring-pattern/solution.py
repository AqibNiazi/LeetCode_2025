class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # First, calculate the length of the string
        n = len(s)

        # Iterate over possible substring lengths starting from n//2 down to 1
        # A repeating substring cannot be longer than half of the original string
        for l in range(n//2, 0, -1):

            # Check if the substring length divides the string length exactly
            # If it does not divide evenly, it cannot form the whole string
            if n % l == 0:

                # Calculate how many times the substring must repeat
                times = n // l

                # Extract the candidate substring pattern
                pattern = s[:l]

                # Initialize a new string that will be built by repeating the pattern
                newStr = ""

                # Repeat the pattern 'times' number of times
                while times > 0:
                    newStr += pattern

                    # If the constructed string matches the original string
                    # then the string is formed by repeating this substring
                    if newStr == s:
                        return True

                    # Decrease the remaining repetitions
                    times -= 1

        # If no repeating pattern reconstructs the string, return False
        return False