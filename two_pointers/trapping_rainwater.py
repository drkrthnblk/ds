https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        res = 0
        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        
        while l < r:
            # the lower bound will be the threshold
            # use that to calculate the curr position and update the curr pos
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
                
        return res