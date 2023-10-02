https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, h = 0, len(height) - 1
        max_water = 0
        while l < h:
            curr_max = min(height[l], height[h]) * (h - l)
            max_water = max(max_water, curr_max)
            if height[l] < height[h]:
                l += 1
            else:
                h -= 1
        return max_water