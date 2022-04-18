https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = list()
        if numRows == 1:
            return [[1]]
        else:
            for i in range(numRows):
                if i == 0:
                    res.append([1])
                elif i == 1:
                    res.append([1,1])
                else:
                    last_entry = res[-1]
                    tmp =[1]
                    for j in range(len(last_entry)-1):
                        tmp.append(last_entry[j]+last_entry[j+1])
                    tmp.append(1)
                    res.append(tmp)
            return res