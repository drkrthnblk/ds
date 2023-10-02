https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, h = 0, len(numbers) - 1
        while l < h:
            curr_sum = numbers[l] + numbers[h]
            if curr_sum == target:
                return [l+1, h+1]
            elif curr_sum < target:
                l += 1
            else:
                h -= 1