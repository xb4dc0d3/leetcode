class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        
        if n == 0: return False
        
        res = n & (n-1)
        if res == 0: return True
        return False
