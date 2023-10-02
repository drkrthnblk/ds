https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        if len(nums) < 3:
            return res
        for idx in range(len(nums)-1):
            # consecutive ele can't be same
            # as i and j will be same
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            l = idx + 1
            r = len(nums) -1
            while l < r:
                curr_sum = nums[idx] + nums[l] + nums[r]
                if curr_sum == 0:
                    res.append([nums[idx] ,nums[l] ,nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
        return res