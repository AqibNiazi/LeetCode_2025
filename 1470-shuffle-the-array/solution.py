
# Solution 1: Using a new array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result
   
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
# Solution 2 : Using Bit manipulation

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i+n]  #store x, y
        
        j = 2 * n - 1
        for i in range(n-1, -1, -1):
            y = nums[i] & (2**10 - 1)
            x = nums[i] >> 10
            nums[j] = y
            nums[j-1] = x
            j -= 2
        return nums

  


    
        