https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if there is nothing in second list, nothing to do
        if n!=0:
            total_len = len(nums1)-1
            m -= 1
            n -= 1
            while total_len >= 0:
                # if second list ele is > first list ele or nothing n first list
                # use the second list ele
                if nums1[m] < nums2[n] or m < 0:
                    nums1[total_len] = nums2[n]
                    n-=1
                    # if the second list is empty then everyting is done
                    if n<0:
                        break
                else:
                    nums1[total_len] = nums1[m]
                    m-=1
                total_len -= 1