https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack, max_area = [], 0

        # add ele until we encounter inc order
        # for dec pop the ele and calculate the max area
        # move the index to the latest popped ele index
        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                prev_idx, pre_height = stack.pop()
                max_area = max(max_area, pre_height*(idx-prev_idx))
                start = prev_idx
            stack.append((start, height))

        # we will end up with some elements that can be extended till the end
        # calculate the area for each of them
        # since each of them can be extended to the right the width is 
        # max index - curr index
        for idx, height in stack:
            max_area = max(max_area, height*(len(heights) - idx))
        
        return max_area