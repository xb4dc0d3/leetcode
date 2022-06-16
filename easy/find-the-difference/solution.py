class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        
        arr_s = sorted(list(s))
        arr_t = sorted(list(t))
        
        
        for i in range(0, len(arr_t)):
            
            if len(arr_s)-1  < i:
                arr_s.append("")
                
                
            if arr_t[i] != arr_s[i]:
                return arr_t[i]
