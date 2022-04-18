https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required = {}
        for i in range(len(nums)):
            # if target is in the final dict then return
            if target - nums[i] in required:
                return [required[target - nums[i]],i]
            else:
                # target is not found in dict, add curr ele idx and move forward
                required[nums[i]]=i