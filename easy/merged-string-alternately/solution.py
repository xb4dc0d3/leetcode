class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        
        merged_string = ""
        turn = len(word1)
        
        
        if len(word1) > len(word2):
            turn = len(word1)
            
        elif len(word1) < len(word2):
            turn = len(word2)
        
        
        
        idx = 0
        while idx != turn:
            
            
            if len(word1)-1 < idx:
                merged_string += ""+ word2[idx]
                
            elif len(word2)-1 < idx:
                merged_string += word1[idx] + ""
                
            else:
                merged_string += word1[idx] + word2[idx]
            
            idx += 1
            
        return merged_string
        
