https://leetcode.com/problems/number-of-1-bits/description/

# solution 1: using shift operator and and logic

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # check if the last bit of n is 1 by anding it with 1
            if n & 1 == 1:
                count += 1
            # shift the bits to right by 1 to get the next bit at least value pos
            n = n >> 1
        return count
		
# solution 2: using and logic
class Solution:
    def hammingWeight(self, n: int) -> int:
		# anding n with n-1 removes the leftmost 1 bit(next set bit from left)
		# so everytime we do this we remove one 1 bit and hence we inc count
		# once all 1 bits are removed th loop end and we don't have to traverse every bit
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res