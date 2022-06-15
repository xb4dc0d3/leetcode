class Solution:
    def isSafe(self, s1, s2):
        dict_s1 = {}
        dict_s2 = {}
        for i in s1:
            dict_s1[i] = dict_s1.get(i,0) + 1
        
        for i in s2:
            dict_s2[i] = dict_s2.get(i,0) + 1
            
        return dict_s1 == dict_s2
            
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        for i in range(len(s2)-len(s1)+1):
            if self.isSafe(s1, s2[i:i+len(s1)]):
                return True
        
        return False
