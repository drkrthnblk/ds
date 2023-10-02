https://leetcode.com/problems/missing-number/description/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = nums[0]
        
        for ele in nums[1:]:
            num ^= ele
            
        
        for i in range(len(nums)+1):
            num ^= i
        
        return num