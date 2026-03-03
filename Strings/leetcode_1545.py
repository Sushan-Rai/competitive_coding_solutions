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