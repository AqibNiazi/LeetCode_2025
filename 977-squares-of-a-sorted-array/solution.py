class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                result.append(nums[l] * nums[l])
                l += 1
            else:
                result.append(nums[r] * nums[r])
                r -= 1
        return result[::-1]

        
        # Time Complexity: O(n)
        # Space Complexity: O(n)