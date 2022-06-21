class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        accumulator = 0
        
        for num in nums:
            accumulator ^= num
            
        return accumulator
