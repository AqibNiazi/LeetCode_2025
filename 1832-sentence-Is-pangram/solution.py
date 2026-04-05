# 1️⃣ Brute Force Solution 

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch not in sentence:
                return False
        return True
    
# 2️⃣ Better Approach — Using Set

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26