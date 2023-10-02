https://leetcode.com/problems/longest-consecutive-sequence/description/


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        numSet = set(nums)
        
        for num in nums:
            if num-1 not in numSet:
                curr_len = 1
                while num+1 in numSet:
                    curr_len += 1
                    num += 1
                max_len = max(max_len, curr_len)
        return max_len