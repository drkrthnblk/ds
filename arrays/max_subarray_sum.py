https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # store the first arr val
        curr_sum, max_sum = nums[0], nums[0]
        
        # loop over the rest
        for i in range(1,len(nums)):
            #  get the max of curr sum or curr sum + curr value
            curr_sum = max(nums[i], curr_sum+nums[i])
            # get max of curr sum or max sum
            max_sum = max(curr_sum, max_sum)
        return max_sum