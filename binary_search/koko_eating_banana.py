https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the max time can never be more than the time to eat max pile
        # hence high = max(piles)
        low, high = 1, max(piles)

        # calculate the total time taken if taken mid of ranged time
        # based on binary search
        while low < high:
            mid = (low + high)//2
            total_time = sum(math.ceil(pile/mid) for pile in piles)

            if total_time > h:
                low = mid + 1
            else:
                high = mid
        return low