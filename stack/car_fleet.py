https://leetcode.com/problems/car-fleet/description/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair, reverse=True):
            # calculate time it will take for each to
            stack.append((target-p)/s)
            # even if a car is faster if it's behind a slow car
            # it will be clubbed as one, that's why we started in reverse position
            # thus all the ones taking same time can be clubbed together
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)