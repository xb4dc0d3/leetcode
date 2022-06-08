# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left_idx = 0
        right_idx = n
        ans = 1
        
        if n == 1:
            return 1
        
        while left_idx <= right_idx:
            middle_idx = left_idx + (right_idx - left_idx) // 2
            
            
            if isBadVersion(middle_idx) == True:
                ans = middle_idx
                right_idx =  middle_idx - 1
                
            else:
                left_idx = middle_idx + 1
                
        return ans
