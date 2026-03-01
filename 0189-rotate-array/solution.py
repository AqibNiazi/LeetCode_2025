class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Step 1: Reverse the original array
        # Step 2: Reverse the 1st k elements 
        # Step 3: Reverse the remaining portion of the array
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1  # Array Reversal complete here
        
        l, r = 0 ,k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1  # 1st K elements reversal complete here
        
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1  # remaing K elements reversal complete here


        
        """
        Do not return anything, modify nums in-place instead.
        """
        