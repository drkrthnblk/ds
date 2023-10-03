https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high)//2

            # if mid is > high then left is sorted and low is on right side
            # as we will have a drop somewhere in the right side
            # low = mid + 1 to break the while loop
            if nums[mid] > nums[high]:
                low = mid + 1
            # right is sorted and low is on left side
            # if mid - 1 we might miss the min
            else:
                high = mid
        return nums[low]
        