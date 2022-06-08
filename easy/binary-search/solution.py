class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left_idx = 0
        right_idx = len(nums) - 1
        
        while left_idx <= right_idx:
            middle_idx = left_idx + ((right_idx - left_idx) // 2)
            
            if target == nums[middle_idx]:
                return middle_idx
            
            elif target > nums[middle_idx]:
                left_idx = middle_idx + 1
                
            else:
                right_idx = middle_idx - 1

        return -1
