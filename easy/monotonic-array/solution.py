class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        flag_inc = True
        flag_dec = True
        
        
        # don't need to include the same number because we care only the progression
        
        for i in range(len(nums)):
            
            if i != len(nums) - 1:
                # monotone increasing
                if nums[i] < nums[i+1]:
                    flag_dec = False


                # monotone decreasing
                if nums[i] > nums[i+1]:
                    flag_inc = False
                
        
        return flag_inc or flag_dec
