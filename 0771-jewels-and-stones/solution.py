#  Solution 1:
#  Time : O(n * m)    
#  Space : O(1)
 class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_count = 0
        for ch in stones:
            if ch in jewels:
                jewels_count += 1
        return jewels_count
            


        
#  Solution 2:
#  Time : O(n + m)
#  Space : O(n)
 class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        jewels_count = 0
        for ch in stones:
            if ch in jewels_set:
                jewels_count += 1
        return jewels_count