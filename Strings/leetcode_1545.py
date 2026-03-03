'''
For this problem pattern recognition is important take small examples like s1 s2 s3 and see the pattern since
the string length had a limit of 2^20 - 1 it makes sense that this uses binary search. but one evident pattern
was the mid ele was alternating with one and zero when moved either left or right, and if we find the mid ele then 
we return if we exit out the reverse of the mid element is sent as the result.
'''
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        mid_ele = 1
        left = 1
        right = 2**n - 1
        while left < right:
            mid = (left + right) // 2
            if mid == k:
                return str(mid_ele)
            elif mid > k:
                right = mid - 1
                mid_ele = 1
            else:
                left = mid + 1
                mid_ele = 0
        res = mid_ele ^ 1
        return str(res)