https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r, c = len(matrix), len(matrix[0])
        
        for i in range(r):
            if matrix[i][0] <= target <= matrix[i][c-1]:
                found = self.bin_srch(matrix[i][:], target)
                if found:
                    return True
        return False
    
    def bin_srch(self, arr: List[int], target: int) -> bool:
        l, h = 0, len(arr)-1
        while l<=h:
            mid = (h + l)//2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid+1
            else:
                h = mid-1
        return False