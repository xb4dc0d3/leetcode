class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left_idx = 0
        right_idx = len(nums) - 1
        
        while left_idx <= right_idx:
            middle_idx = left_idx + (right_idx - left_idx) // 2
            
            if target == nums[middle_idx]:
                return middle_idx
            
            elif target > nums[middle_idx]:
                left_idx = middle_idx + 1
                
            else:
                right_idx = middle_idx - 1
                
                
        if target > nums[right_idx]:
            right_idx = right_idx + 1

            if right_idx > len(nums) - 1:
                return len(nums)
            else:
                return right_idx
        
        if target < nums[left_idx]:
            left_idx = left_idx - 1

            if left_idx < 0:
                return 0
            else:
                return left_idx
