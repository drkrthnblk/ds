https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


#sol1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        local_minima = [0]*len(prices)
        local_maxima = [0]*len(prices)
        
        # find local minima
        temp = prices[0]
        local_minima[0] = temp
        for i in range(1,len(prices)):
            if prices[i]>temp:
                local_minima[i] = temp
            else:
                temp = prices[i]
                local_minima[i] = temp

        # find local maxima
        temp = prices[-1]
        local_maxima[-1] = temp
        for i in range(len(prices)-2, -1, -1):
            if prices[i]<temp:
                local_maxima[i] = temp
            else:
                temp = prices[i]
                local_maxima[i] = temp
        
        
        # find the max profit for each index
        res = 0
        for i  in range(len(local_maxima)):
            if local_maxima[i] - local_minima[i] > res:
                res = local_maxima[i] - local_minima[i]
        return res
            
#sol2

class Solution:
    def maxProfit(prices):
        diff=0
        currSum=0
        maxSum=0
        for i in range(len(pices)-1):
            diff=prices[i+1]-prices[i]
            if currSum>0:
                currSum+=diff
            else: 
                currSum=diff
            if maxSum<currSum:
                maxSum=currSum
        return maxSum