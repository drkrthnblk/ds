https://leetcode.com/problems/contains-duplicate/

# solution 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # sort the list
        nums.sort()
        
        # loop oer the list and check if consecutive ele are same or not
        # if found just return true then and there
        found = True
        prev = nums[0]
        for ele in nums[1:]:
            if ele == prev:
                return True
            prev = ele
        return False
        

# solution 2:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for ele in nums:
            if ele in visited:
                return True
            visited.add(ele)
        return False