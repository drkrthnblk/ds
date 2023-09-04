https://leetcode.com/problems/find-the-duplicate-number/description/

# solution 1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for ele in nums:
            if nums[abs(ele)] < 0:
                return abs(ele)
            nums[abs(ele)] = - nums[abs(ele)]
			
			
# solution 2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find the "entrance" to the cycle.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow