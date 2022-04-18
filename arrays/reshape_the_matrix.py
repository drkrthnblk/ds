https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        
        res = [[0 for _ in range(c)] for _ in range(r)]
        
        curr_r, curr_c = 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[curr_r][curr_c] = mat[i][j]
                curr_c += 1

                if curr_c == c:
                    curr_c = 0
                    curr_r += 1

        return res
                    