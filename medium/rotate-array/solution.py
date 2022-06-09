class Solution:
    def rotate(self, nums, k: int) -> None:
        
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
            return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if k > n:
            k = k % n

        # reverse the last n-k elements
        reverse(nums, n-k, n-1)

        # reverse the first n-k elements
        reverse(nums, 0, n-k-1)

        # reverse the whole list
        reverse(nums, 0, n-1)

        return nums
        
