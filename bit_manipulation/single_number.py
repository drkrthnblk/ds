https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for ele in nums[1:]:
            res ^= ele
        return res