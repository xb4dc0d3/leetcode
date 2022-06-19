class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        arr = []
        pointer = 0
        
        for numToCheck in nums1:
            for idx in range(len(nums2)):
                pointer = 0
            
                if numToCheck == nums2[idx]:
                    
                    # check next element
                    pointer = idx
                    while pointer != len(nums2) - 1:
                        if numToCheck < nums2[pointer+1]:
                            arr.append(nums2[pointer+1])
                            break
                        
                        pointer += 1
                    
                    if pointer == len(nums2) - 1:
                        arr.append(-1)
                
                
                        
        return arr
